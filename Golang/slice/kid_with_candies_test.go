package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestKidWithCandies(t *testing.T) {
	expected := []bool{true, true, true, false, true}
	candies := []int{2, 3, 5, 1, 3}
	extraCandies := 3

	assert.EqualValues(t, expected, slice.KidsWithCandies(candies, extraCandies))
}
