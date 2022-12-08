# Class
class Directory:
    # constructor
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []
        self.files = []

    # functions
    def print(self, space):
        indent = ' ' + space
        print(space + '- ' + self.name + ' (dir) ' + str(self.getsize()))
        for q in self.children:
            q.print(indent)

            for r in self.files:
                r.print(indent)

    def addfile(self, x):
        self.files.append(x)

    def addchild(self, x):
        self.children.append(x)

    def getparent(self):
        return self.parent

    def getchild(self, x):
        for q in self.children:
            if q.name == x:
                return q
        print('no child found')

    def getsize(self):
        size = 0
        for q in self.files:
            size += int(q.size)
        for r in self.children:
            size += r.getsize()
        return size

    def undersize(self, x, filesize):
        for q in self.children:
            q.undersize(x, filesize)
        if self.getsize() <= filesize:
            x.append(self)

    def oversize(self, x, filesize):
        for q in self.children:
            q.oversize(x, filesize)
        if self.getsize() >= filesize:
            x.append(self)


class File:
    # constructor
    def __init__(self, name, size, directory):
        self.name = name
        self.size = size
        self.directory = directory

    def print(self, space):
        print(space + '- ' + self.name + ' (file, size=' + self.size + ')')


# Functions
def part1(outerdir):
    counter = []
    totalSize = 0
    outerdir.undersize(counter, 100000)
    for q in counter:
        totalSize += q.getsize()
    print(str(totalSize))
    return


def part2(outerdir):
    counter = []
    sizeOfOptions = []
    totalDiskSpace = 70000000
    spaceNeeded = 30000000
    spaceTaken = outerdir.getsize()
    spaceToFreeUp = spaceNeeded - (totalDiskSpace - spaceTaken)
    outerdir.oversize(counter, spaceToFreeUp)
    for q in counter:
        sizeOfOptions.append(q.getsize())
    print(str(min(sizeOfOptions)))
    return


# Main
topLevel = Directory('/', [])
currentDirectory = topLevel

f = open('inputs\\day7Input.txt', 'r')
lines = f.read().split('\n')
f.close()

for i in lines:  # make tree
    instructions = i.split(' ')
    if instructions[0] == 'dir':
        currentDirectory.addchild(Directory(instructions[1], currentDirectory))  # add a new child based on name given
    elif instructions[0] == '$':
        if instructions[1] == 'cd':
            if instructions[2] == '..':
                currentDirectory = currentDirectory.getparent()  # go back to parent
            else:
                currentDirectory = currentDirectory.getchild(
                    (instructions[2]))  # go into child object that matches the name
    else:
        currentDirectory.addfile(File(instructions[1], instructions[0], currentDirectory))

part2(topLevel)
