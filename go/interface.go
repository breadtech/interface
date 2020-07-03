package breadinterface

import (
	"context"
)

// Input declares methods for reading input.
type Input interface {
	// Scan infinitely reads input from some source and sends events down the channel.
	Scan(context.Context, chan<- string) error
}

// Logic declares methods for handling events.
type Logic interface {
	// Handle processes the given event and signals a render down the channel.
	Handle(context.Context, context.CancelFunc, string, chan<- bool) error
}

// Output declares methods for writing output.
type Output interface {
	// Logic.Handle renders the buffer.
	Logic

	// Print flushes the buffer to a target output device.
	Print(context.Context) error
}
