package day2

import (
	"fmt"
	"strings"

	"github.com/cktang88/aoc2020/util"
)

// Run Problem 2
func Run(lines []string) {
	arr := make([][]string, len(lines))

	goodPasswords := 0
	for i, a := range lines {
		chunks := strings.Split(a, " ")
		// util.PrintArray(&chunks)

		bounds := strings.Split(string(chunks[0]), "-")
		key := string(chunks[1])[0]
		s := chunks[2]

		// fmt.Println(bounds, key, s)
		matches := 0
		for _, c := range s {
			if c == rune(key) {
				matches++
			}
		}
		low := util.IntParse(bounds[0])
		high := util.IntParse(bounds[1])

		// part 1
		// if matches >= low && matches <= high {
		// 	goodPasswords++
		// }

		// part 2
		if (s[low-1] == key) != (s[high-1] == key) {
			goodPasswords++
		}

		arr[i] = chunks
	}
	fmt.Println(goodPasswords)
}
