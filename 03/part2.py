import collections

def groupsFrom(fileName):
    with open(fileName) as input:
        groups = []
        currentGroup = []
        for line in input:
            currentGroup.append(set(line.strip()))

            if len(currentGroup) == 3:
                groups.append(currentGroup)
                currentGroup = []

        return groups


def badgeFromGroup(group):
    (badge, ) = set.intersection(*group)

    return badge


def priorityFromBadge(badge):
    ordinal = ord(badge)

    if ordinal > 90:
        return ordinal - 96

    return ordinal - 38


groups = groupsFrom('input.txt')

total = 0
for group in groups:
    badge = badgeFromGroup(group)
    total += priorityFromBadge(badge)

print(total)

