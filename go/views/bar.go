package views

import ()

// NewBar returns a new bar
func NewBar() Interface {
	return new(Bar)
}

// Bar
type Bar struct {
	View
}

// Unmarshal specially handles the buttons field.
func (b *Bar) Unmarshal(dat Map) error {
	if err := b.View.Unmarshal(dat); err != nil {
		return err
	}

	buttons, ok := dat["buttons"].([]interface{})
	if !ok {
		return nil
	}

	b.subviews = make([]Interface, len(buttons))
	for i, button := range buttons {
		b.subviews[i] = NewButton()
		if err := b.subviews[i].Unmarshal(button.(Map)); err != nil {
			return err
		}
	}
	return nil
}
