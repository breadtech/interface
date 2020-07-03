package termbox

import (
	"context"

	"github.com/nsf/termbox-go"

	bi "breadinterface"
)

type Mapping struct {
	Key, Action string
}

type Scanner struct {
	bi.Input
	mappings []bi.Mapping
}

func (scanner *Scanner) Scan(ctx context.Context, msgCh chan<- string) error {
	log := log.WithField("func", "termbox.scanner.Scan")
	errCh := make(chan error)
	go func(errCh chan error) {
		for {
			ev := termbox.PollEvent()
			log.WithField("event", ev).Debug("received event")
			switch ev.Type {
			case termbox.EventInterrupt:
				errCh <- nil
			case termbox.EventError:
				errCh <- ev.Err
			default:
				msgCh <- string(ev.Ch)
			}
		}
	}(errCh)

	select {
	case err := <-errCh:
		close(errCh)
		return err
	case <-ctx.Done():
		return nil
	}
}
