with open('Day8/input.txt', 'r') as file:
    lines = file.readlines()
network = {}
import math
for lineInd in range(2,len(lines)):
    line = lines[lineInd]
    key = line[0:3]
    to = line.split('=')[1].split(',')
    left = to[0][2:].strip()
    right = to[1][:len(to[1])-2].strip()
    dict = {}
    dict['L'] = left
    dict['R'] = right 
    network[key] = dict
instructions = lines[0].strip()
print(len(instructions))

startKeys = []
for key,value in network.items():
    if key[2] == 'A':
        startKeys.append(key)
print(startKeys)
CountsAndZs = []
for startKey in startKeys:
    instructCount = 0
    instructInd = 0
    cont = True
    key = startKey
    while cont:
        if key[2] == 'Z':
            cont = False
            break
        if instructInd >= len(instructions):
            instructInd = 0
        instruction = instructions[instructInd]
        next = network[key][instruction]
        key = next
        instructCount += 1
        instructInd += 1
    CountsAndZs.append([[instructCount, key]])


def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            print(cache)
            return cache[args]
        result = func(*args)
        print('Adding', result, 'to the cache')
        cache[args] = result
        return result
    return wrapper

@memoize
def getNextZ(instructInd, currentZ):
    instructCount = 0
    cont = True
    key = currentZ
    while cont:
        instructInd = instructInd % len(instructions)
        instruction = instructions[instructInd]
        next = network[key][instruction]
        key = next
        instructCount += 1
        instructInd += 1
        if key[2] == 'Z':
            cont = False
            return [instructCount, key]

Zhits = []
for ZandCount in CountsAndZs:
    Zhits.append([ZandCount[0][0]])
print([num[0] for num in Zhits])
print(math.lcm(*[num[0] for num in Zhits]))
print()
print(Zhits)
iteration = 0
cont = True
while cont:
    #Check if new numbers appear in all other lists
    for ghostInd in range(len(Zhits)):
        newestZhitCount = Zhits[ghostInd][iteration]
        inAll = True
        for i in range(len(Zhits)):
            if newestZhitCount not in Zhits[i]:
                inAll = False
                break
        if inAll:
            print(newestZhitCount)
            cont = False
            break
    #Get new CountsAndZs and Zhits
    for ghostPathInd in range(len(CountsAndZs)):
        instructInd = CountsAndZs[ghostPathInd][iteration][0] % len(instructions)
        print(CountsAndZs[ghostPathInd][iteration][0])
        print(instructInd)
        [countToAdd, newZ] =  getNextZ(instructInd, CountsAndZs[ghostPathInd][iteration][1])
        CountsAndZs[ghostPathInd].append([countToAdd + CountsAndZs[ghostPathInd][iteration][0], newZ])
        Zhits[ghostPathInd].append(countToAdd + CountsAndZs[ghostPathInd][iteration][0])
    iteration += 1