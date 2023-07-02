package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestLeftRightDifference(t *testing.T) {
	expected := []int{15, 1, 11, 22}
	nums := []int{10, 4, 8, 3}

	assert.Equal(t, expected, slice.LeftRightDifference(nums))
}
