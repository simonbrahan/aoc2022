import re

def parseInput(fileName):
    with open(fileName) as file:
        fileContents = file.read()

    start, instructions = fileContents.split('\n\n')

    return parseCrates(start), parseInstructions(instructions)


def parseCrates(crates):
    out = {}
    for line in crates.split('\n'):
        for idx, char in enumerate(line):
            if not char.isalpha():
                continue

            pileIdx = int((idx + 3) / 4)

            if pileIdx not in out:
                out[pileIdx] = []

            out[pileIdx].append(char)

    for pile in out:
        out[pile].reverse()

    return out


def parseInstructions(instructions):
    out = []
    for line in instructions.split('\n'):
        if len(line) == 0:
            continue

        out.append([int(num) for num in re.split('move | from | to ', line)[1:]])

    return out


def moveCrates(crates, numCrates, fromPileIdx, toPileIdx):
    for i in range(numCrates):
        crates[toPileIdx].append(crates[fromPileIdx].pop())


def topCrates(crates):
    out = ''
    for _, crate in sorted(crates.items()):
        out += crate[-1]

    return out


crates, instructions = parseInput('input.txt')

for numCrates, fromPile, toPile in instructions:
    moveCrates(crates, numCrates, fromPile, toPile)

print(topCrates(crates))
