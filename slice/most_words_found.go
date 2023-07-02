package slice

import (
	"unicode"
)

func MostWordsFound(sentences []string) int {
	result := 0
	for _, sentence := range sentences {
		words := countWords(sentence)
		if words > result {
			result = words
		}
	}
	return result
}

func countWords(sentence string) int {
	words := 1
	for _, char := range sentence {
		if unicode.IsSpace(char) {
			words++
		}
	}
	return words
}
