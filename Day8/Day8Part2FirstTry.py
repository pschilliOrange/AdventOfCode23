with open('Day8/input.txt', 'r') as file:
    lines = file.readlines()
import sys
sys.setrecursionlimit(3000)
from functools import lru_cache
network = {}
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
instructCount = 0
instructInd = 0
startKeys = []
for key,value in network.items():
    if key[2] == '':
        startKeys.append(key)
steps = []


@lru_cache(maxsize=None)
def getNextStep(key, instructInd):
    if key[2] == 'Z':
        return 1
    if instructInd >= len(instructions):
        instructInd = 0
    instruction = instructions[instructInd]
    next = network[key][instruction]
    return getNextStep(next, instructInd + 1) + 1

print(startKeys)
for startingKey in startKeys:
    steps.append(getNextStep(startingKey,0))
print(steps)
print(max(steps))