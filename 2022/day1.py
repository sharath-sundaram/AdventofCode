# Imports
import numpy as np


# Helper Functions
# Part 1
def part1(array1):
    elfMaxCal = array1[array1.argmax(axis=0)]
    print("The maximum amount of calories held by a single elf is " + str(elfMaxCal))
    return


# Part 2
def part2(array2):
    top3 = array2[np.argpartition(array2, -3)[-3:]]
    print("The total amount of calories held by the top 3 elves is " + str(np.sum(top3)) + " calories")
    return


# Main
f = open('inputs\\day1Input.txt', 'r')
lines = f.read().split('\n')
f.close()

calTotal = 0
elfTotal = []
for i in lines:
    if i:
        calTotal += int(i)
    else:
        elfTotal.append(calTotal)
        calTotal = 0
elfCal = np.array(elfTotal)
part1(elfCal)
