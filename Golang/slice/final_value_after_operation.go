package slice

func FinalValueAfterOperation(operations []string) int {
	opsMap := map[string]int{
		"X++": 1,
		"++X": 1,
		"X--": -1,
		"--X": -1,
	}
	result := 0
	for _, operation := range operations {
		result += opsMap[operation]
	}
	return result
}
