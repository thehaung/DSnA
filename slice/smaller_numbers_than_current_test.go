package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestSmallerNumbersThanCurrent(t *testing.T) {
	expected := []int{4, 0, 1, 1, 3}
	nums := []int{8, 1, 2, 2, 3}

	assert.Equal(t, expected, slice.SmallerNumberThanCurrent(nums))
}
