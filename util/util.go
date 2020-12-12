package util

import (
	"fmt"
	"strconv"
	"strings"
)

// Check handles error
func Check(e error) {
	if e != nil {
		panic(e)
	}
}

// FindInSortedArray finds a value in a sorted array
// Returns (index, value) if found, (-1, -1) if not found
func FindInSortedArray(arr *[]int, val int) (int, int) {
	for i, n := range *arr {
		if n == val {
			return i, n
		}
		if n > val {
			break
		}
	}
	return -1, -1
}

// PrintArray prints comma separated array
func PrintArray(arr *[]string) {
	output := "'" + strings.Join(*arr, `','`) + `'`
	fmt.Println(output)
}

// IntParse forcibly parses a string into an int
func IntParse(s string) int {
	num, err := strconv.Atoi(s)
	Check(err)
	return num
}
