package main

import (
	"context"
	"os"

	bi "breadinterface"
	"breadinterface/termbox"
	"breadinterface/views"
)

func main() {
	var (
		frameCfgPath string
		mappingPath  string
	)
	if len(os.Args) > 1 {
		frameCfgPath = os.Args[1]
	} else {
		frameCfgPath = "configs/frame.yaml"
	}
	if len(os.Args) > 2 {
		mappingPath = os.Args[2]
	} else {
		mappingPath = "configs/mapping.yaml"
	}

	if err := termbox.Init(); err != nil {
		panic(err)
	}
	defer termbox.Close()

	ctx := context.Background()
	input := new(termbox.Scanner)
	engine := new(Engine)

	controller := views.NewController(termbox.NewRenderer())
	if err := controller.(*views.Controller).LoadFromConfig(frameCfgPath); err != nil {
		panic(err)
	}

	mapping, err := bi.LoadMapping(mappingPath)
	if err != nil {
		panic(err)
	}

	if err := bi.Run(ctx, input, engine, controller, mapping); err != nil {
		panic(err)
	}
}

type Engine struct {
}

func (e *Engine) Handle(ctx context.Context, cancel context.CancelFunc, msg string, redraw chan<- bool) error {
	if msg == "q" {
		cancel()
		return nil
	}
	return nil
}
