package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestNumIdenticalPairs(t *testing.T) {
	expected := 4
	nums := []int{1, 2, 3, 1, 1, 3}
	assert.Equal(t, expected, slice.NumIdenticalPairs(nums))
}
