import numpy as np
with open('Day18/sample.txt', 'r') as file:
    lines = file.readlines()
height = 1
count = 0
prevAdd = 1
firstDirection = int(lines[0].split(' ')[2][7])
for i in range(len(lines)):
    direction = int(lines[i].split(' ')[2][7])
    num = int(lines[i].split(' ')[2][2:7], 16)
    if i+1 == len(lines):
        nextDirection = firstDirection
    else:
        nextDirection = int(lines[i+1].split(' ')[2][7])
    print(direction, num)
    if direction == 2: #left
        if nextDirection == 1:
            add = 1
        else:
            add = 0
        count = count - height*(num-1+add+prevAdd)
    elif direction == 0: #right
        if nextDirection == 3:
            add = 1
        else:
            add = 0
        count = count + height*(num-1+add+prevAdd)
    elif direction == 1: #down
        if nextDirection == 0:
            add = 1
        else:
            add = 0
        height = height - (num-1+add+prevAdd)
    elif direction == 3: #up
        if nextDirection == 2:
            add = 1
        else:
            add = 0
        height = height + (num-1+add+prevAdd)
    prevAdd = add
print(count)

