import re

def rangesFromFile(fileName):
    with open(fileName) as file:
        ranges = [list(map(int, re.split(',|-', line.strip()))) for line in file]

    return ranges


def rangePairOverlaps(rangePair):
    [aStart, aEnd, bStart, bEnd] = rangePair

    if aStart <= bStart and aEnd >= bEnd:
        return True

    if aStart >= bStart and aEnd <= bEnd:
        return True

    return False


ranges = rangesFromFile('input.txt')

overlapCount = 0
for rangePair in ranges:
    if rangePairOverlaps(rangePair):
        overlapCount += 1

print(overlapCount)
