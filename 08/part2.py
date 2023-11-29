def getTrees(fileName):
    with open(fileName) as file:
        return [list(map(int, list(line.strip()))) for line in file]


def countVisible(trees, start, direction):
    x, y = start
    xDir, yDir = direction

    thisTreeHeight = trees[y][x]
    visibleCount = 0
    while 0 < y < len(trees)-1 and 0 < x < len(trees[y])-1:
        x += xDir
        y += yDir

        visibleCount += 1

        if trees[y][x] >= thisTreeHeight:
            break


    return visibleCount


trees = getTrees('input.txt')
forestWidth = len(trees[0])
forestLength = len(trees)
highScore = 0

for x in range(forestWidth):
    for y in range(forestLength):
        visibleDown = countVisible(trees, (x, y), (0, 1))
        score = visibleDown

        visibleUp = countVisible(trees, (x, y), (0, -1))
        score *= visibleUp

        visibleLeft = countVisible(trees, (x, y), (1, 0))
        score *= visibleLeft

        visibleRight = countVisible(trees, (x, y), (-1, 0))
        score *= visibleRight

        highScore = max(highScore, score)

print(highScore)
