package slice

import (
	"fmt"
	"math"
)

/*
	expected := []int{15, 1, 11, 22}
	nums := []int{10, 4, 8, 3}
*/

func LeftRightDifference(nums []int) []int {
	leftSum, rightSum := 0, 0
	for _, num := range nums {
		rightSum += num
	}
	for i, num := range nums {
		rightSum -= num
		fmt.Printf("rightSum: %d, leftSum: %d\n", rightSum, leftSum)
		nums[i] = int(math.Abs(float64(leftSum - rightSum)))
		leftSum += num
	}
	return nums
}
