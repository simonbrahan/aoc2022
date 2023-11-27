def firstMarkerPosFor(line):
    for idx, char in enumerate(line):
        if startOfPacket(idx, line):
            return idx + 1

    return None


def startOfPacket(idx, line):
    if idx < 4:
        return False

    checkedChars = set()

    for i in range(4):
        if line[idx-i] in checkedChars:
            return False

        checkedChars.add(line[idx-i])

    return True


with open('input.txt') as file:
    for line in file:
        print(firstMarkerPosFor(line))
