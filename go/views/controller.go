package views

import (
	"context"
	"io/ioutil"
	"os"

	"github.com/sirupsen/logrus"
	"gopkg.in/yaml.v2"
	metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"

	bi "breadinterface"
)

type ControllerSpec struct {
	metav1.TypeMeta   `json:",inline"`
	metav1.ObjectMeta `json:"metadata"`
	Spec              Map `json:"spec"`
}

type Controller struct {
	Frame Interface `json:"main"`
	Renderer
}

func NewController(r Renderer) bi.Output {
	f := NewFrame()
	f.SetRect(Rect{Point{}, r.GetSize()})
	return &Controller{
		Frame:    f,
		Renderer: r,
	}
}

func (c *Controller) UnmarshalYAML(unmarshal func(interface{}) error) error {
	dat := make(logrus.Fields)
	if err := unmarshal(dat); err != nil {
		return err
	}
	c.Frame = NewFrame()
	return c.Frame.Unmarshal(dat["main"].(map[interface{}]interface{}))
}

func (c *Controller) Print(ctx context.Context) error {
	if err := c.Frame.Layout(); err != nil {
		return err
	}
	if err := c.Frame.Render(ctx, c.Renderer); err != nil {
		return err
	}
	return nil
}

func (c *Controller) Handle(ctx context.Context, cancel context.CancelFunc, msg string, redraw chan<- bool) error {
	/*
		next := f.selection

		// determine next selection based on msg.
		switch msg {
		case "up":
			next -= 1
		case "down":
			next += 1
		case "left":
			next -= 1
		case "right":
			next += 1
		}

		// exit here if selection hasn't changed.
		if next == f.selection {
			log.Debug("passing")
			return nil
		}

		f.selection = next
		redraw <- true
	*/

	return nil
}

// LoadController returns a Controller from the yaml file given by path.
func (c *Controller) LoadFromConfig(path string) error {
	log := log.WithField("func", "LoadFromConfig")
	log.Trace("+")
	defer log.Trace("-")

	f, err := os.Open(path)
	if err != nil {
		log.WithError(err).Error("failed to open file")
		return err
	}

	b, err := ioutil.ReadAll(f)
	if err != nil {
		log.WithError(err).Error("failed to read file")
		return err
	}
	log.WithField("dat", string(b)).Debug("read file")

	spec := new(ControllerSpec)
	if err := yaml.Unmarshal(b, spec); err != nil {
		log.WithError(err).Error("failed to unmarshal config")
		return err
	}

	return c.Frame.Unmarshal(spec.Spec["main"].(Map))
}
