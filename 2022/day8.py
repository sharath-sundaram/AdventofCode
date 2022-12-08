# Helper Functions
def checknorth(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    for q in range(0, y):
        if trees[q][x] >= treeHeight:
            isHighest = False
    return isHighest


def checksouth(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    for q in range(y + 1, gridlength):
        if trees[q][x] >= treeHeight:
            isHighest = False
    return isHighest


def checkeast(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    scenicScore = 0
    for q in range(x + 1, gridlength):
        if trees[y][q] >= treeHeight:
            isHighest = False
    return isHighest


def checkwest(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    scenicScore = 0
    for q in range(0, x):
        if trees[y][q] >= treeHeight:
            isHighest = False
    return isHighest


def scorenorth(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    scenicScore = 0
    for q in reversed(range(0, y)):
        if isHighest:
            scenicScore += 1
            if trees[q][x] >= treeHeight:
                isHighest = False
    return scenicScore


def scoresouth(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    scenicScore = 0
    for q in range(y + 1, gridlength):
        if isHighest:
            scenicScore += 1
            if trees[q][x] >= treeHeight:
                isHighest = False
    return scenicScore


def scoreeast(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    scenicScore = 0
    for q in range(x + 1, gridlength):
        if isHighest:
            scenicScore += 1
            if trees[y][q] >= treeHeight:
                isHighest = False
    return scenicScore


def scorewest(trees, x, y, gridlength):
    treeHeight = trees[y][x]
    isHighest = True
    scenicScore = 0
    for q in reversed(range(0, x)):
        if isHighest:
            scenicScore += 1
            if trees[y][q] >= treeHeight:
                isHighest = False
    return scenicScore


# Functions
# Part 1
def part1(trees):
    visibleTrees = 0
    treeGridLength = len(trees)
    edgeTrees = (2 * treeGridLength) + (2 * (treeGridLength - 2))  # automatically count trees at the edges
    for q in range(1, treeGridLength - 1):
        for r in range(1, treeGridLength - 1):
            if checknorth(trees, r, q, treeGridLength):
                visibleTrees += 1
            elif checksouth(trees, r, q, treeGridLength):
                visibleTrees += 1
            elif checkeast(trees, r, q, treeGridLength):
                visibleTrees += 1
            elif checkwest(trees, r, q, treeGridLength):
                visibleTrees += 1
    print(int(visibleTrees + edgeTrees))
    return


# Part 2
# Trees on the edges will not be considered since one of the scenic scores is 0 resulting in final score of 0
def part2(trees):
    treeGridLength = len(trees)
    scoreMax = 0
    for q in range(1, treeGridLength - 1):
        for r in range(1, treeGridLength - 1):
            score = (scorenorth(trees, r, q, treeGridLength) * scoresouth(trees, r, q, treeGridLength) *
                     scoreeast(trees, r, q, treeGridLength) * scorewest(trees, r, q, treeGridLength))
            if score > scoreMax:
                scoreMax = score
    print(scoreMax)


# Main
f = open('inputs\\day8Input.txt', 'r')
lines = f.read().split('\n')
f.close()

treeGrid = []
gridRange = range(len(lines))
for i in lines:
    treeGrid.append([j for j in i])

part2(treeGrid)
