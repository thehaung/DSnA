package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestFinalValueAfterOperations(t *testing.T) {
	expected := 3
	ops := []string{"X--", "X++", "++X", "++X", "X++"}

	assert.Equal(t, expected, slice.FinalValueAfterOperation(ops))
}
