package main

import "fmt"

func main() {
	fmt.Println(leftSum([]int{10, 4, 8, 3}))
}

func rightSum(nums []int) []int {
	result := make([]int, len(nums))
	for i := len(nums) - 2; i > 0; i-- {
		result[i] = result[i-1] + nums[i]
	}
	return result
}

func leftSum(nums []int) []int {
	result := make([]int, len(nums))
	for i := 1; i < len(nums); i++ {
		result[i] = result[i-1] + nums[i]
	}
	return result
}
