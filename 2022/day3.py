# Helper Functions
# Part 1
def part1(array1):
    totalSum = 0
    for i in lines:
        comp1 = []
        comp2 = []
        letters = [j for j in i]
        for k in range(0, len(letters)):
            if k < (len(letters) / 2):
                comp1.append(letters[k])
            else:
                comp2.append(letters[k])
        commonL = str(list(set(comp1) & set(comp2))[0])
        if commonL.islower():
            totalSum += (ord(commonL) - 96)
        else:
            totalSum += (ord(commonL) - 38)
    print("The total sum of the items would be " + str(totalSum))
    return


# Part 2
def part2(array2):
    totalSum = 0
    elf1 = array2[0::3]
    elf2 = array2[1::3]
    elf3 = array2[2::3]

    for i in range(len(elf1)):
        letters1 = set([x for x in elf1[i]])
        letters2 = set([y for y in elf2[i]])
        letters3 = set([z for z in elf3[i]])
        commonL = str(list(letters1 & letters2 & letters3)[0])
        if commonL.islower():
            totalSum += (ord(commonL) - 96)
        else:
            totalSum += (ord(commonL) - 38)
    print("The total sum of the items would be " + str(totalSum))
    return


# Main
f = open('inputs\\day3Input.txt', 'r')
lines = f.read().split('\n')
f.close()

part2(lines)
