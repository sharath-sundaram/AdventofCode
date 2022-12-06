# Functions
# Part 1
def part1():
    lastFour = [' ', ' ', ' ', ' ']
    counter = 0
    with open('inputs\\day6Input.txt') as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of File")
                break
            counter += 1
            lastFour.pop(0)
            lastFour.append(c)
            if (len(list(set(lastFour))) == 4) & (lastFour[0] != ' '):
                print(lastFour)
                print(counter)
                break
    return


# Part 2
def part2():
    lastFourteen = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    counter = 0
    with open('inputs\\day6Input.txt') as f:
        while True:
            c = f.read(1)
            if not c:
                print("End of File")
                break
            counter += 1
            lastFourteen.pop(0)
            lastFourteen.append(c)
            if (len(list(set(lastFourteen))) == 14) & (lastFourteen[0] != ' '):
                print(lastFourteen)
                print(counter)
                break
    return


# Main
part2()




