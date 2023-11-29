def getTrees(fileName):
    with open(fileName) as file:
        return [list(map(int, list(line.strip()))) for line in file]


def checkForVisible(trees, start, direction):
    x, y = start
    xDir, yDir = direction

    visible = set()
    lastVisible = -1
    while 0 <= y < len(trees) and 0 <= x < len(trees[y]):
        if trees[y][x] > lastVisible:
            visible.add((x, y))
            lastVisible = trees[y][x]

        x += xDir
        y += yDir

    return visible


trees = getTrees('input.txt')
forestWidth = len(trees[0])
forestLength = len(trees)
visible = set()

for x in range(forestWidth):
    visibleDown = checkForVisible(trees, (x, 0), (0, 1))
    visible.update(visibleDown)
    visibleUp = checkForVisible(trees, (x, forestLength-1), (0, -1))
    visible.update(visibleUp)

for y in range(forestLength):
    visibleLeft = checkForVisible(trees, (0, y), (1, 0))
    visible.update(visibleLeft)
    visibleRight = checkForVisible(trees, (forestWidth-1, y), (-1, 0))
    visible.update(visibleRight)

print(len(visible))

