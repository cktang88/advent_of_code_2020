package day1

import (
	"fmt"
	"sort"
	"strconv"

	"github.com/cktang88/aoc2020/util"
)

// Run Problem 1
func Run(lines []string) {

	// last line is always newline
	arr := make([]int, len(lines))
	for i, s := range lines {
		val, err := strconv.Atoi(s)
		util.Check(err)
		arr[i] = val
	}
	// sort arr
	sort.Ints(arr)
	// fmt.Println(arr)

	/*
		part 1
	*/
	for _, a := range arr {
		ind, b := util.FindInSortedArray(&arr, 2020-a)
		if ind > -1 {
			fmt.Println(a, b, a*b)
			break
		}
	}

	/*
		part 2
	*/
	for _, a := range arr {
		found := false
		for _, b := range arr {
			if a+b > 2020 {
				break
			}
			ind, c := util.FindInSortedArray(&arr, 2020-a-b)
			if ind > -1 {
				fmt.Println(a, b, c, a*b*c)
				found = true
				break
			}
		}
		if found {
			break
		}
	}
}
