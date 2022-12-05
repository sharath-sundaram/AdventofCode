# Functions
# Part 1
def part1(x, y):
    for q in y:
        instructSplit = q.split(' ')
        amount = int(instructSplit[1])
        startRow = int(instructSplit[3]) - 1
        endRow = int(instructSplit[5]) - 1
        for r in range(amount):
            x[endRow].append(x[startRow].pop())
    topCrate = []
    for s in x:
        topCrate.append(s.pop())
    print(
        topCrate[0] + topCrate[1] + topCrate[2] + topCrate[3] + topCrate[4] + topCrate[5] + topCrate[6] + topCrate[7] +
        topCrate[8])
    return


# Part 2
def part2(x, y):
    for q in y:
        instructSplit = q.split(' ')
        amount = int(instructSplit[1])
        startRow = int(instructSplit[3]) - 1
        endRow = int(instructSplit[5]) - 1
        popIndex = len(x[startRow]) - amount
        for r in range(amount):
            x[endRow].append(x[startRow].pop(popIndex))
    topCrate = []
    for s in x:
        topCrate.append(s.pop())
    print(
        topCrate[0] + topCrate[1] + topCrate[2] + topCrate[3] + topCrate[4] + topCrate[5] + topCrate[6] + topCrate[7] +
        topCrate[8])

    return


# Main
f = open('inputs\\day5Input.txt', 'r')
lines = f.read().split('\n')
f.close()

baseState = []
modState = []
instructions = []
for i in range(len(lines)):
    if i < 8:
        baseState.insert(0, lines[i])
    elif i > 9:
        instructions.append(lines[i])

for j in range(0, 9):
    stack = []
    for k in baseState:
        characters = [l for l in k]
        if characters[(j * 4) + 1] != ' ':
            stack.append(characters[(j * 4) + 1])
    modState.append(stack)
part1(modState, instructions)
