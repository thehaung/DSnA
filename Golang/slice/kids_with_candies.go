package slice

func KidsWithCandies(candies []int, extraCandies int) []bool {
	result := make([]bool, len(candies))
	greateNums := GetMaxCandies(candies)
	for i, candy := range candies {
		if candy+extraCandies >= greateNums {
			result[i] = true
		}
	}
	return result
}

func GetMaxCandies(candies []int) int {
	result := 0
	for _, candy := range candies {
		if candy > result {
			result = candy
		}
	}
	return result
}
