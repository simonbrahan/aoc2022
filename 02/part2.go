package main

import (
	"bufio"
	"fmt"
	"os"
)

type game struct {
	strategy   rune
	theirs rune
}

func gameFromStr(input string) game {
	splitInput := []rune(input)
	return game{strategy: splitInput[2], theirs: splitInput[0]}
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
		game{'X', 'A'}: 0 + 3,
		game{'X', 'B'}: 0 + 1,
		game{'X', 'C'}: 0 + 2,
		game{'Y', 'A'}: 3 + 1,
		game{'Y', 'B'}: 3 + 2,
		game{'Y', 'C'}: 3 + 3,
		game{'Z', 'A'}: 6 + 2,
		game{'Z', 'B'}: 6 + 3,
		game{'Z', 'C'}: 6 + 1,
	}

	return outcomes[g]
}

func main() {
	games := gamesFromInput()

	score := 0
	for _, currentGame := range games {
		score += scoreFrom(currentGame)
	}

	fmt.Println(score)
}
