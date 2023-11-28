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


def sumOfSmallDirs(directories):
    total = 0

    for _, dirSize in directories.values():
        if dirSize <= 100000:
            total += dirSize

    return total


current = ()
directories = {}

with open('input.txt') as file:
    for line in file:
        current = parse(line, directories, current)

print(sumOfSmallDirs(directories))
