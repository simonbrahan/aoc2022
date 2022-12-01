package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func main() {
	inputFile, _ := os.Open("input.txt")
	defer inputFile.Close()

	lines := bufio.NewScanner(inputFile)

	calorieCounts := []int{}
	currentElfCount := 0
	for lines.Scan() {
		line := lines.Text()

		if line == "" {
			calorieCounts = append(calorieCounts, currentElfCount)
			currentElfCount = 0
			continue
		}

		calories, _ := strconv.Atoi(line)
		currentElfCount += calories
	}

	calorieCounts = append(calorieCounts, currentElfCount)

	first := 0
	second := 0
	third := 0
	for _, calorieCount := range calorieCounts {
		if calorieCount > third {
			third = calorieCount
		}

		if calorieCount > second {
			second, third = calorieCount, second
		}

		if calorieCount > first {
			first, second = calorieCount, first
		}
	}

	fmt.Println(first)
	fmt.Println(second)
	fmt.Println(third)

	fmt.Println(first + second + third)
}
