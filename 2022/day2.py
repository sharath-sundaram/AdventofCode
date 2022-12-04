# Helper Functions
# Part 1
def part1(list1):
    scoreDict = {
        'A X': 4,
        'A Y': 8,
        'A Z': 3,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 7,
        'C Y': 2,
        'C Z': 6,
    }
    pointTotal1 = 0
    for i in list1:
        pointTotal1 += scoreDict[str(i)]
    print("The total score following the strategy guide would be " + str(pointTotal1) + "pts")
    return


# Part 2
def part2(list2):
    scoreDict = {
        'A X': 3,
        'A Y': 4,
        'A Z': 8,
        'B X': 1,
        'B Y': 5,
        'B Z': 9,
        'C X': 2,
        'C Y': 6,
        'C Z': 7,
    }
    pointTotal2 = 0
    for i in list2:
        pointTotal2 += scoreDict[str(i)]
    print("The total score following the strategy guide would be " + str(pointTotal2) + "pts")
    return


# Main
f = open('inputs\\day2Input.txt', 'r')
lines = f.read().split('\n')
f.close()

part2(lines)
