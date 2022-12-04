# Functions
# Part 1
def part1(x):
    subsets = 0
    for i in x:
        assignments = i.split(',')
        range1 = assignments[0].split('-')
        range2 = assignments[1].split('-')
        set1 = set(range(int(range1[0]), int(range1[1])+1))
        set2 = set(range(int(range2[0]), int(range2[1])+1))
        if set1.issubset(set2) or set2.issubset(set1):
            subsets += 1

    print("There are " + str(subsets) + " pairings that contain a subset of the other")
    return


# Part 2
def part2(x):
    subsets = 0
    for i in x:
        assignments = i.split(',')
        range1 = assignments[0].split('-')
        range2 = assignments[1].split('-')
        set1 = set(range(int(range1[0]), int(range1[1]) + 1))
        set2 = set(range(int(range2[0]), int(range2[1]) + 1))
        if set1 & set2:
            subsets += 1

    print("There are " + str(subsets) + " pairings that share an index")
    return


# Main
f = open('inputs\\day4Input.txt', 'r')
lines = f.read().split('\n')
f.close()

part2(lines)


