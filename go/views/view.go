package views

import (
	"context"
	"fmt"
)

func NewView() Interface {
	return new(View)
}

// View is the base implementation of a renderable object.
type View struct {
	rect      Rect
	kind      string
	flow      Flow
	subviews  []Interface
	selected  bool
	selection int
	weight    int
}

// Rect is Rect.
func (v *View) Rect() Rect {
	return v.rect
}

// SetRect sets the Rect.
func (v *View) SetRect(r Rect) {
	v.rect = r
}

// Kind is string as kind.
func (v *View) Kind() string {
	return v.kind
}

// Weight is int as weight.
func (v *View) Weight() int {
	return v.weight
}

// Flow is string as flow.
func (v *View) Flow() Flow {
	return v.flow
}

// Subviews is an array of subviews.
func (v *View) Subviews() []Interface {
	return v.subviews
}

// IsSelected is a bool.
func (v *View) IsSelected() bool {
	return v.selected
}

// Select handles the select signal.
func (v *View) Select() string {
	// Forward select to selection if already selected.
	if v.selected {
		return v.subviews[v.selection].Select()
	}
	// Select if not yet selected.
	v.selected = true
	return ""
}

// Move handles the move signal.
func (v *View) Move(dir bool) {
	if v.selected {
		// First iterate over subviews to forward move if selected.
		for _, view := range v.subviews {
			if view.IsSelected() {
				view.Move(dir)
				return
			}
		}
		// Move internal selection pointer and handle over/underflows..
		n := len(v.subviews)
		if dir && v.flow == FlowLR || dir && v.flow == FlowTB {
			v.selection++
			if v.selection == n {
				v.selection = 0
			}
		} else {
			v.selection--
			if v.selection == -1 {
				v.selection = n - 1
			}
		}
	}
}

// Cancel handles the cancel signal.
func (v *View) Cancel() {
	// First see if a subview is selected to cancel.
	for _, view := range v.subviews {
		if view.IsSelected() {
			v.subviews[v.selection].Cancel()
			return
		}
	}
	// If no subviews are selected then deselected this view.
	v.selected = false
}

// Layout lays out its subviews' rects and forwards the Layout call to them.
func (v *View) Layout() error {
	log := log.WithField("func", "View.Layout")
	log.Trace("+")
	defer log.Trace("-")

	// Sum the weights and determine max
	totalWeight := 0
	max := 0
	for _, sv := range v.subviews {
		w := sv.Weight()
		totalWeight += w
		if w > max {
			max = w
		}
	}

	// Scale out the sizes
	unitSize := v.rect.ScaleDown(totalWeight, totalWeight)
	sizes := make([]Size, len(v.subviews))
	totalScaledWidth := 0
	totalScaledHeight := 0
	for i, sv := range v.subviews {
		sizes[i] = unitSize.ScaleUp(sv.Weight(), sv.Weight())
		totalScaledWidth += sizes[i].W
		totalScaledHeight += sizes[i].H
	}

	// Determine if any left over points and give remainder to largest weight subview.
	if dWidth := v.rect.W - totalScaledWidth; dWidth > 0 {
		for i, sv := range v.subviews {
			if sv.Weight() == max {
				sizes[i].W += dWidth
			}
		}
	}

	if dHeight := v.rect.H - totalScaledHeight; dHeight > 0 {
		for i, sv := range v.subviews {
			if sv.Weight() == max {
				sizes[i].H += dHeight
			}
		}
	}

	// Set the rects of subviews based on flow and weight/totalWeight
	next := 0
	switch v.flow {
	case FlowLR:
		for i, sv := range v.subviews {
			log := log.WithField("i", i)
			log.Trace("+subview")
			r := v.rect
			r.X += next
			r.Size.W = sizes[i].W
			sv.SetRect(r)
			next = r.X + r.W
			log.Trace("-subview")
		}
		break
	case FlowRL:
		break
	case FlowTB:
		for i, sv := range v.subviews {
			log.WithField("i", i)
			log.Trace("+subview")
			r := v.rect
			r.Y += next
			r.Size.H = sizes[i].H
			sv.SetRect(r)
			next = r.Y + r.H
			log.Trace("-subview")
		}
		break
	case FlowBT:
		break
	}

	// Call layout to subviews
	for _, sv := range v.subviews {
		if err := sv.Layout(); err != nil {
			return err
		}
	}
	return nil
}

// Render tells the passed in renderer how to draw itself
//   and forwards it to the subviews.
func (v *View) Render(ctx context.Context, r Renderer) error {
	r.RenderRect(ctx, v.rect, v.selected)

	for _, sv := range v.subviews {
		if err := sv.Render(ctx, r); err != nil {
			return err
		}
	}
	return nil
}

func (v *View) Unmarshal(dat Map) error {
	log := log.WithField("func", "View.Unmarshal")
	log.WithField("dat", len(dat)).Trace("+")
	defer log.Trace("-")

	var ok bool
	// Extract kind as string
	if v.kind, ok = dat["kind"].(string); !ok {
		v.kind = "view"
	}
	log.WithField("kind", v.kind).Trace("parsed")

	// Extract flow as string
	flowStr, ok := dat["flow"].(string)
	if !ok {
		flowStr = string(FlowLR)
	}
	v.flow = Flow(flowStr)
	log.WithField("flow", v.flow).Trace("parsed")

	// weight as int
	if v.weight, ok = dat["weight"].(int); !ok {
		v.weight = 1
	}
	log.WithField("weight", v.weight).Trace("parsed")

	// subviews as an array of map[interface{}]interface{}
	svs, ok := dat["subviews"].([]interface{})
	if !ok {
		v.subviews = []Interface{}
	}
	log.WithField("subviews", len(v.subviews)).Trace("parsed")

	// iterate over subviews data and unmarshal them.
	n := len(svs)
	v.subviews = make([]Interface, n)
	for i, svInt := range svs {
		svDat := svInt.(Map)
		subkind, ok := svDat["kind"].(string)
		if !ok {
			subkind = "view"
		}
		newFunc, ok := kindToNewView[subkind]

		if !ok {
			return fmt.Errorf("subview %d has invalid kind %s", i, subkind)
		}
		v.subviews[i] = newFunc()
		if err := v.subviews[i].Unmarshal(svDat); err != nil {
			return err
		}
	}
	return nil
}

// UnmarshalYAML
func (v *View) UnmarshalYAML(unmarshal func(interface{}) error) error {
	log := log.WithField("func", "View.UnmarshalYAML")
	log.Trace("+")
	defer log.Trace("-")

	dat := make(Map)
	if err := unmarshal(dat); err != nil {
		return err
	}
	if err := v.Unmarshal(dat); err != nil {
		return err
	}
	return nil
}
