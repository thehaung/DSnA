package slice

func NumIdenticalPairs(nums []int) int {
	result := 0
	numMap := map[int]int{}
	for _, num := range nums {
		result += numMap[num]
		numMap[num] = numMap[num] + 1
	}
	return result
}
