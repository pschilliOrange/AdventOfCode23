with open('Day14/input.txt', 'r') as file:
    lines = file.readlines()
import math
import copy
platform = []
platform.append(['#']*(len(lines[0])+1))
for lineInd in range(len(lines)):
    line = '#' + lines[lineInd].strip() + '#'
    platform.append(list(line))
platform.append(['#']*(len(lines[0])+1))

def moveOneUp(platform):
    notDone = False
    for rowInd in range(1, len(platform)):
        for colInd in range(len(platform[0])):
            if platform[rowInd][colInd] == 'O' and platform[rowInd - 1][colInd] == '.':
                notDone = True
                platform[rowInd][colInd] = '.'
                platform[rowInd-1][colInd] = 'O'
    return platform, notDone

def moveOneRight(platform):
    notDone = False
    for rowInd in range(1, len(platform)):
        for colInd in range(len(platform[0])):
            if platform[rowInd][colInd] == 'O' and platform[rowInd][colInd + 1] == '.':
                notDone = True
                platform[rowInd][colInd] = '.'
                platform[rowInd][colInd + 1] = 'O'
    return platform, notDone

def moveOneDown(platform):
    notDone = False
    for rowInd in range(1, len(platform)):
        for colInd in range(len(platform[0])):
            if platform[rowInd][colInd] == 'O' and platform[rowInd+1][colInd] == '.':
                notDone = True
                platform[rowInd][colInd] = '.'
                platform[rowInd+1][colInd] = 'O'
    return platform, notDone

def moveOneLeft(platform):
    notDone = False
    for rowInd in range(1, len(platform)):
        for colInd in range(len(platform[0])):
            if platform[rowInd][colInd] == 'O' and platform[rowInd][colInd-1] == '.':
                notDone = True
                platform[rowInd][colInd] = '.'
                platform[rowInd][colInd-1] = 'O'
    return platform, notDone

def spin(platform):
    cont = True
    while cont:
        platform, cont = moveOneUp(platform)
    cont = True
    while cont:
        platform, cont = moveOneLeft(platform)
    cont = True
    while cont:
        platform, cont = moveOneDown(platform)
    cont = True
    while cont:
        platform, cont = moveOneRight(platform)
    return platform

weights = []
configurations = []
configuration = copy.deepcopy(platform)
platform = []
platform = copy.deepcopy(spin(configuration))
weight = 0
for rowInd in range(1, len(platform)):
    for colInd in range(len(platform)):
        if platform[rowInd][colInd] == 'O':
            weight += (len(platform) - 1) - rowInd
weights.append(weight)
configurations.append(copy.deepcopy(platform))

weights = []
num = 1000000000 - 1
cont = True
while cont:
    configuration = []
    configuration = copy.deepcopy(platform)
    platform = []
    platform = copy.deepcopy(spin(configuration))
    if platform in configurations:
        cycleLength = len(configurations) - configurations.index(platform)
        numOfSpinsAfterStartOfCycle = (num - len(configurations)) % cycleLength
        cont = False 
        break
    weight = 0
    for rowInd in range(1, len(platform)):
        for colInd in range(len(platform)):
            if platform[rowInd][colInd] == 'O':
                weight += (len(platform) - 1) - rowInd
    weights.append(weight)
    configurations.append(copy.deepcopy(platform))
print(weights[configurations.index(platform) + numOfSpinsAfterStartOfCycle -1 ])



'''
weight = 0
#count
print()
for row in platform:
    print(row)
for rowInd in range(1, len(platform)):
    for colInd in range(len(platform)):
        if platform[rowInd][colInd] == 'O':
            print((len(platform) - 1) - rowInd)
            weight += (len(platform) - 1) - rowInd
print(weight)'''

             

