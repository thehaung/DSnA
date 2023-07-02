package slice_test

import (
	"testing"

	"github.com/stretchr/testify/assert"
	"github.com/thehaung/DSnA/slice"
)

func TestMaximumWealth(t *testing.T) {
	expected := 6
	accounts := [][]int{{1, 2, 3}, {3, 2, 1}}
	assert.Equal(t, expected, slice.MaximumWealth(accounts))
}
