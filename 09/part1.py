def parseInput(filename):
    out = []
    with open(filename) as file:
        for line in file:
            [direction, steps] = line.strip().split(' ')
            out.append((direction, int(steps)))

    return out


def handleMove(headPos, tailPos, tailVisited, direction, steps):
    directions = {'U': (0, 1), 'R': (1, 0), 'D': (0, -1), 'L': (-1, 0)}

    xMove, yMove = directions[direction]

    for i in range(steps):
        headPos = (headPos[0] + xMove, headPos[1] + yMove)
        tailPos = seek(headPos, tailPos)
        tailVisited.add(tailPos)

    return headPos, tailPos


def seek(headPos, tailPos):
    if touching(headPos, tailPos):
        return tailPos

    newTailX = tailPos[0]
    if newTailX > headPos[0]:
        newTailX -= 1
    if newTailX < headPos[0]:
        newTailX += 1

    newTailY = tailPos[1]
    if newTailY > headPos[1]:
        newTailY -= 1
    if newTailY < headPos[1]:
        newTailY += 1

    return (newTailX, newTailY)


def touching(headPos, tailPos):
    touchingX = abs(headPos[0] - tailPos[0]) <= 1
    touchingY = abs(headPos[1] - tailPos[1]) <= 1

    return touchingX and touchingY


moves = parseInput('input.txt')

headPos = (0, 0)
tailPos = (0, 0)
tailVisited = set()

for direction, steps in moves:
    headPos, tailPos = handleMove(headPos, tailPos, tailVisited, direction, steps)

print(len(tailVisited))
