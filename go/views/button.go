package views

import (
	"fmt"
)

// Button ...
type Button struct {
	TextView
	OnClick string
}

// NewButton ...
func NewButton() Interface {
	return new(Button)
}

// Unmarshal specially handles the onclick field.
func (b *Button) Unmarshal(dat Map) error {
	if err := b.TextView.Unmarshal(dat); err != nil {
		return err
	}

	if onclick := dat["onclick"]; onclick != nil {
		var ok bool
		if b.OnClick, ok = onclick.(string); !ok {
			return fmt.Errorf("onclick field should be string")
		}
	}
	return nil
}
