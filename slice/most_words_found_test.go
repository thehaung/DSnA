package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestMostWordsFound(t *testing.T) {
	expected := 5
	sentences := []string{"ja ja ja", "ah ha", "ha ha ha ha ha"}
	assert.Equal(t, expected, slice.MostWordsFound(sentences))
}
