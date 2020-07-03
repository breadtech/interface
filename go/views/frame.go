package views

import (
	"context"
)

// NewFrame creates a Frame instance with the given window Rect.
func NewFrame() Interface {
	return new(Frame)
}

// Frame is a view that takes up the whole window.
type Frame struct {
	View `json:",inline" yaml:",inline"`
}

// Render determines the proper placing of its inner components.
func (f *Frame) Render(ctx context.Context, r Renderer) error {
	log := log.WithField("func", "Frame.Render")
	log.Trace("+")
	defer log.Trace("-")

	r.Clear()
	if err := f.View.Render(ctx, r); err != nil {
		return err
	}
	return r.Print(ctx)
}
