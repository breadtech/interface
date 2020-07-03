package views

import (
	"context"

	bi "breadinterface"
)

var (
	defaultBarHeight = 3
	log              = bi.Log
)

type Map map[interface{}]interface{}

// Renderer declares the methods required to Print on a target Window.
type Renderer interface {
	bi.Output
	GetSize() Size

	Clear()
	RenderChar(context.Context, Point, rune)
	RenderRect(context.Context, Rect, bool)
}

// Interface declares the methods necessary to use for Output.Print
type Interface interface {
	Rect() Rect
	SetRect(Rect)

	Kind() string
	Weight() int
	Flow() Flow
	Subviews() []Interface

	IsSelected() bool
	Select() string
	Move(bool)
	Cancel()

	Layout() error
	Render(ctx context.Context, r Renderer) error

	Unmarshal(Map) error
}

var (
	kindToNewView = map[string]func() Interface{
		"bar":    NewBar,
		"button": NewButton,
		"text":   NewTextView,
		"view":   NewView,
		"frame":  NewFrame,
	}
)
