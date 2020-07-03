package breadinterface

import (
	"io/ioutil"
	"os"

	"gopkg.in/yaml.v2"
)

// Mapping defines an implementation specific event key to a contextual action.
type Mapping map[string]string

// LoadMapping returns a Mapping from the yaml file given by path.
func LoadMapping(path string) (Mapping, error) {
	f, err := os.Open(path)
	if err != nil {
		return nil, err
	}

	b, err := ioutil.ReadAll(f)
	if err != nil {
		return nil, err
	}

	mapping := make(Mapping)
	if err := yaml.Unmarshal(b, &mapping); err != nil {
		return nil, err
	}

	return mapping, nil
}
