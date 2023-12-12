import numpy as np
with open('Day5/example2.txt', 'r') as file:
    content = file.read()
# Splitting the content into lines
lines = content.splitlines()
seedsWithSpaces = lines[0].split(':')[1].split(' ')
seeds =  [int(elem) for elem in seedsWithSpaces if elem != '']
currentMap = []
max = 0
locations = []
sameMap = 1
for y in seeds:
    seed = y
    for i in range(0,len(lines)):
        line = lines[i]
        if line == '':
            continue
        if not line[0].isdigit():
            sameMap = 1
            continue
        if sameMap == 0:
            continue
        numsWithSpaces = []
        numsWithSpaces = lines[i].split(' ')
        nums = []
        nums =  [int(elem) for elem in numsWithSpaces if elem != '']
        if nums[1] <= y and y < nums[1]+nums[2]:
            y = nums[0]+(y-nums[1])
            sameMap = 0
        
    locations.append(y)
        #if sameMap = 0:
print(locations)
#print(min(locations))