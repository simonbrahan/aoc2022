package main

import (
	"bufio"
	"errors"
	"fmt"
	"os"
)

type pack struct {
	left map[rune]int
	right map[rune]int
}

func packFromStr(input string) pack {
	splitAt := len(input) / 2
	leftInput := input[:splitAt]
	rightInput := input[splitAt:]

	left := map[rune]int{}
	for _, char := range leftInput {
		left[char]++
	}

	right := map[rune]int{}
	for _, char := range rightInput {
		right[char]++
	}

	return pack{left, right}
}

func packsFromInput() []pack {
	inputFile, _ := os.Open("input.txt")
	defer inputFile.Close()

	lines := bufio.NewScanner(inputFile)

	packs := []pack{}
	for lines.Scan() {
		p := packFromStr(lines.Text())

		packs = append(packs, p)
	}

	return packs
}

func commonItemFromPack(pack pack) (rune, error) {
	for item, _ := range pack.left {
		_, inRight := pack.right[item]

		if inRight {
			return item, nil
		}
	}

	return 0, errors.New("no duplicate item found")
}

func priorityFromItem(item rune) int {
	if int(item) > 90 {
		return int(item) - 96
	} else {
		return int(item) - 38
	}
}

func main() {
	packs := packsFromInput()

	prioritySum := 0
	for _, pack := range packs {
		commonItem, _ := commonItemFromPack(pack)
		prioritySum += priorityFromItem(commonItem)
	}

	fmt.Println(prioritySum)
}
