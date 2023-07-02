package slice

import "fmt"

/*
expected := []int{4, 0, 1, 1, 3}
nums := []int{8, 1, 2, 2, 3}
*/

func SmallerNumberThanCurrent(nums []int) []int {
	count := make([]int, 101)
	result := make([]int, len(nums))
	for _, num := range nums {
		count[num]++
	}

	fmt.Println(count)
	for i := 1; i < 101; i++ {
		count[i] += count[i-1]
	}

	fmt.Println(count)

	for i, num := range nums {
		if num == 0 {
			result[i] = 0
		} else {
			result[i] = count[num-1]
		}
	}
	return result
}
