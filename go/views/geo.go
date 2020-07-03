package views

// Point defines a 2-dimensional (2D)  (X, Y) coordinate.
type Point struct {
	X, Y int
}

// Shift moves a point by (x, y).
func (p Point) Shift(x, y int) Point {
	p.X += x
	p.Y += y
	return p
}

// Size defines a 2D of length,
//  W: width, H: height
type Size struct {
	W, H int
}

// ScaleUp resizes a size up.
func (s Size) ScaleUp(x, y int) Size {
	s.W *= x
	s.H *= y
	return s
}

// ScaleDown resizes a size down.
func (s Size) ScaleDown(x, y int) Size {
	s.W /= x
	s.H /= y
	return s
}

// Rect defines a rectangle with a Point and a Size.
type Rect struct {
	Point
	Size
}

// Flip defines a 2D flipping flag.
type Flip struct {
	X, Y bool
}

type Flow string

const (
	FlowLR = Flow("lr")
	FlowRL = Flow("rl")
	FlowTB = Flow("tb")
	FlowBT = Flow("bt")
)
