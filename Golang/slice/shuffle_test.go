package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestShuffle(t *testing.T) {
	nums := []int{1, 2, 3, 4, 5, 6}
	expected := []int{1, 4, 2, 5, 3, 6}
	assert.EqualValues(t, expected, slice.Shuffle(nums, 3))
}
