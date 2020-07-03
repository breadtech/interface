package breadinterface

/*
  breadinterface provides a thread-safe i/o process execution engine for
	  code that implements the appropriate interfaces.
*/

import (
	"context"
	"os"
	"os/signal"
	"syscall"
	"time"

	"golang.org/x/sync/errgroup"

	"github.com/sirupsen/logrus"
)

var (
	log     = new(logrus.Logger)
	logFile *os.File

	Log = log
)

func init() {
	// Setup logging.
	var err error
	logFile, err = os.OpenFile("bi.log", os.O_WRONLY|os.O_APPEND|os.O_CREATE, 0755)
	if err != nil {
		panic(err)
	}

	log.SetFormatter(&logrus.JSONFormatter{TimestampFormat: time.StampNano})
	log.SetOutput(logFile)

	logLevelStr := os.Getenv("LOG_LEVEL")
	if logLevel, err := logrus.ParseLevel(logLevelStr); err != nil {
		log.SetLevel(logrus.InfoLevel)
	} else {
		log.SetLevel(logLevel)
	}
}

// Run executes the computational trivium lifecycle.
// Should only ever be called once.
func Run(
	ctx context.Context,
	input Input,
	logic Logic,
	output Output,
	mappings ...Mapping,
) error {
	defer logFile.Close()

	// Setup context.
	ctx, cancel := context.WithCancel(ctx)
	eg, ctx := errgroup.WithContext(ctx)

	// Kill is for os signals.
	kill := make(chan os.Signal)
	signal.Notify(kill, syscall.SIGINT, syscall.SIGTERM)
	eg.Go(func() error {
		log := log.WithField("thread", "sighandler")
		defer close(kill)
		defer signal.Stop(kill)

		log.Debug("listening...")
		select {
		case sig := <-kill:
			log.WithField("sig", sig).Info("killed")
			cancel()
		case <-ctx.Done():
			log.Info("done")
		}
		return nil
	})

	// Run input.Scan to send Events into read.
	read := make(chan string)
	eg.Go(func() error {
		log.WithField("thread", "input").Debug("calling scan")
		return input.Scan(ctx, read)
	})

	// Block on read to send the event to logic.Handle.
	write := make(chan bool)
	eg.Go(func() error {
		log := log.WithField("thread", "logic")
		log.Debug("listening...")
		write <- true // do an initial render.
		for {
			select {
			case <-ctx.Done():
				log.Info("done")
				return nil
			case msg := <-read:
				// Maps msg read from Input to a cmd.
				log.WithField("msg", msg).Trace("received msg")
				for _, mapping := range mappings {
					if mapped, exists := mapping[msg]; exists {
						msg = mapped // to a cmd
						log.WithField("msg", msg).Trace("mapped msg")
					}
				}
				// Logic handles the command.
				if err := logic.Handle(ctx, cancel, msg, write); err != nil {
					log.WithError(err).Error("caught error")
					return err
				}
				// Output renders the buffer.
				if err := output.Handle(ctx, cancel, msg, write); err != nil {
					log.WithError(err).Error("caught error")
					return err
				}
			}
			log.Trace("iter")
		}
	})

	// Run output.Print when the write signal comes in.
	eg.Go(func() error {
		log := log.WithField("thread", "output")
		log.Debug("listening...")
		for {
			select {
			case <-ctx.Done():
				log.Info("done")
				return nil
			case render := <-write:
				// Read render signal from Handle
				log.WithField("render", render).Trace("write")
				if !render {
					continue
				}
				// Output flushes the buffer.
				if err := output.Print(ctx); err != nil {
					log.WithError(err).Error("caught error")
					return err
				}
			}
			log.Trace("iter")
		}
	})

	log.WithField("thread", "main").Debug("waiting...")
	return eg.Wait()
}
