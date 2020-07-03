package views

import (
	"context"
	"fmt"
)

// TextView ...
type TextView struct {
	View
	TextPos Point
	Text    string
}

// NewTextView ...
func NewTextView() Interface {
	return new(TextView)
}

// Layout positions the button on the parent view and sets the text position.
func (tv *TextView) Layout() error {
	r := tv.Rect()
	tv.TextPos = Point{r.X + r.W/2 - len(tv.Text)/2, r.Y + r.H/2}
	return nil
}

// Render draws an outline around the button and renders the text.
func (tv *TextView) Render(ctx context.Context, r Renderer) error {
	// Render outline.
	if err := tv.View.Render(ctx, r); err != nil {
		return err
	}

	// Render text.
	for i, c := range tv.Text {
		r.RenderChar(ctx, tv.TextPos.Shift(i, 0), c)
	}
	return nil
}

// Unmarshal specially handles the text field.
func (tv *TextView) Unmarshal(dat Map) error {
	if err := tv.View.Unmarshal(dat); err != nil {
		return err
	}

	if text := dat["text"]; text != nil {
		var ok bool
		if tv.Text, ok = text.(string); !ok {
			return fmt.Errorf("text field should be string")
		}
	}
	return nil
}
