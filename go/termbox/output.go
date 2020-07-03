package termbox

import (
	"context"

	"github.com/nsf/termbox-go"

	"breadinterface/views"
)

const (
	RuneHorz = rune(0x2550)
	RuneVert = rune(0x2551)

	RuneTL = rune(0x2554)
	RuneTR = rune(0x2557)
	RuneBL = rune(0x255a)
	RuneBR = rune(0x255d)

	Runeㅜ = rune(0x2566)
	Runeㅗ = rune(0x2569)
	Runeㅏ = rune(0x2560)
	Runeㅓ = rune(0x2563)

	RuneMenu = rune(0x2261)
)

func Init() error {
	return termbox.Init()
}

func Close() {
	termbox.Close()
}

type renderer struct {
	fg, bg termbox.Attribute
}

func NewRenderer() views.Renderer {
	return &renderer{
		fg: termbox.ColorWhite,
		bg: termbox.ColorBlack,
	}
}

func (r *renderer) RenderChar(ctx context.Context, pt views.Point, ch rune) {
	termbox.SetCell(pt.X, pt.Y, ch, r.fg, r.bg)
}

func (r *renderer) RenderRect(ctx context.Context, rect views.Rect, highlight bool) {
	fg := r.fg
	if highlight {
		fg = termbox.ColorGreen
	}

	endX := rect.X + rect.W - 1
	endY := rect.Y + rect.H - 1

	// fill background
	for i := 0; i < rect.W; i++ {
		for j := 0; j < rect.H; j++ {
			termbox.SetCell(rect.X+i, rect.Y+j, ' ', fg, r.bg)
		}
	}
	// draw top and bottom lines.
	for i := 0; i < rect.W; i++ {
		termbox.SetCell(rect.X+i, rect.Y, RuneHorz, fg, r.bg)
		termbox.SetCell(rect.X+i, endY, RuneHorz, fg, r.bg)
	}
	// draw left and right lines.
	for j := 0; j < rect.H; j++ {
		termbox.SetCell(rect.X, rect.Y+j, RuneVert, fg, r.bg)
		termbox.SetCell(endX, rect.Y+j, RuneVert, fg, r.bg)
	}

	// draw corners.
	termbox.SetCell(rect.X, rect.Y, RuneTL, fg, r.bg)
	termbox.SetCell(endX, rect.Y, RuneTR, fg, r.bg)
	termbox.SetCell(rect.X, endY, RuneBL, fg, r.bg)
	termbox.SetCell(endX, endY, RuneBR, fg, r.bg)
}

func (r *renderer) GetSize() views.Size {
	w, h := termbox.Size()
	return views.Size{W: w, H: h}
}

func (r *renderer) Clear() {
	termbox.Clear(r.fg, r.bg)
}

func (r *renderer) Print(ctx context.Context) error {
	return termbox.Flush()
}

func (r *renderer) Handle(ctx context.Context, cancel context.CancelFunc, msg string, redraw chan<- bool) error {
	return nil
}
