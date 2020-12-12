package main

import (
	"io/ioutil"
	"strings"

	// "github.com/cktang88/aoc2020/day1"
	"github.com/cktang88/aoc2020/util"

	"github.com/cktang88/aoc2020/day2"
)

func main() {
	// day1.Run(readInputLines("./day1/1.txt"))
	day2.Run(readInputLines("./day2/2.txt"))
}

func readInputLines(filePath string) []string {
	data, err := ioutil.ReadFile(filePath)
	util.Check(err)

	rawArr := strings.Split(string(data), "\n")
	// last line is always empty
	return rawArr[:len(rawArr)-1]
}
