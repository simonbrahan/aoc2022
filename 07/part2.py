def parse(line, directories, current):
    line = line.strip()

    if line.startswith('$ cd'):
        newDir = line.split(' ')[-1]

        if newDir == '..':
            return current[:-1]

        newCurrent = current + (newDir,)

        if newCurrent not in directories:
            directories[newCurrent] = [current, 0]

        return newCurrent

    if line.startswith('$ ls'):
        return current

    if not line.startswith('dir '):
        fileSize = int(line.split(' ')[0])
        incrementDirSizes(directories, current, fileSize)

    return current


def incrementDirSizes(directories, dirPath, fileSize):
    directories[dirPath][1] += fileSize

    parentDir = directories[dirPath][0]
    if parentDir != ():
        incrementDirSizes(directories, parentDir, fileSize)


def findSmallestSuitableDir(directories, requiredCleanup):
    candidateSize = None

    for path, dirSize in directories.values():
        if dirSize < requiredCleanup:
            continue

        if candidateSize == None or dirSize < candidateSize:
            candidateSize = dirSize

    return candidateSize


current = ()
directories = {}

with open('input.txt') as file:
    for line in file:
        current = parse(line, directories, current)

totalSpace = 70000000
requiredSpace = 30000000
availableSpace = totalSpace - directories[('/',)][1]
requiredCleanup = requiredSpace - availableSpace

print(findSmallestSuitableDir(directories, requiredCleanup))
