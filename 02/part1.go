package main

import (
	"bufio"
	"fmt"
	"os"
)

type game struct {
	mine   rune
	theirs rune
}

func gameFromStr(input string) game {
	splitInput := []rune(input)
	return game{mine: splitInput[2], theirs: splitInput[0]}
}

func gamesFromInput() []game {
	inputFile, _ := os.Open("input.txt")
	defer inputFile.Close()

	lines := bufio.NewScanner(inputFile)

	games := []game{}
	for lines.Scan() {
		g := gameFromStr(lines.Text())

		games = append(games, g)
	}

	return games
}

func scoreFrom(g game) int {
	outcomes := map[game]int{
		game{'X', 'A'}: 3,
		game{'X', 'C'}: 6,
		game{'Y', 'A'}: 6,
		game{'Y', 'B'}: 3,
		game{'Z', 'B'}: 6,
		game{'Z', 'C'}: 3,
	}

	choiceBonuses := map[rune]int{
		'X': 1,
		'Y': 2,
		'Z': 3,
	}

	return outcomes[g] + choiceBonuses[g.mine]
}

func main() {
	games := gamesFromInput()

	score := 0
	for _, currentGame := range games {
		score += scoreFrom(currentGame)
	}

	fmt.Println(score)
}
