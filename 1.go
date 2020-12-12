package main

import (
	"fmt"
	"io/ioutil"
	"sort"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

// Finds a value in a sorted array
// Returns (index, value) if found, (-1, -1) if not found
func findInSortedArray(arr *[]int, val int) (int, int) {
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

func main() {
	data, err := ioutil.ReadFile("./1.txt")
	check(err)

	rawArr := strings.Split(string(data), "\n")
	// last line is always newline
	arr := make([]int, len(rawArr)-1)
	for i, s := range rawArr {
		s := strings.Trim(s, " ")
		if len(s) == 0 {
			continue
		}
		val, err := strconv.Atoi(s)
		check(err)
		arr[i] = val
	}
	// sort arr
	sort.Ints(arr)
	// fmt.Println(arr)

	/*
		part 1
	*/
	for _, a := range arr {
		ind, b := findInSortedArray(&arr, 2020-a)
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
			ind, c := findInSortedArray(&arr, 2020-a-b)
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
