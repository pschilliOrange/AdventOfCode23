import numpy as np
with open('Day18/sample.txt', 'r') as file:
    lines = file.readlines()
size = 20
array = np.zeros((size, size))
start = [int(size/2), int(size/2)]
position = start
for line in lines:
    direction = line.split(' ')[0]
    num = int(line.split(' ')[1])
    if direction == 'L':
        for i in range(-1, -num-1, -1):
            array[position[0] + i][position[1]] = 1
        position = [position[0]-num, position[1]]
    elif direction == 'R':
        for i in range(1, num+1):
            array[position[0] + i][position[1]] = 1
        position = [position[0]+num, position[1]]
    elif direction == 'D':
        for i in range(-1, -num-1, -1):
            array[position[0]][position[1] + i] = 1
        position = [position[0], position[1]-num]
    elif direction == 'U':
        for i in range(1, num+1):
            array[position[0]][position[1] + i] = 1
        position = [position[0], position[1]+num]
insideCount = 0
perimeterCount = 0
inside = -1
cumilation = 0
for row in range(size):
    for col in range(size):
        #Upper left
        if array[row][col] == 1 and array[row+1][col] == 1 and array[row][col+1] == 1:
            cumilation += 1/2
            if cumilation == 1:
                inside = inside*-1
                cumilation = 0
        #Upper right
        elif array[row][col] == 1 and array[row][col-1] == 1 and array[row+1][col] == 1:
            cumilation -= 1/2
            if cumilation == -1:
                inside = inside*-1
                cumilation = 0
        #Lower left
        elif array[row][col] == 1 and array[row-1][col] == 1 and array[row][col+1] == 1:
            cumilation -= 1/2
            if cumilation == -1:
                inside = inside*-1
                cumilation = 0
        #Lower right
        elif array[row][col] == 1 and array[row][col-1] == 1 and array[row-1][col] == 1:
            cumilation += 1/2
            if cumilation == 1:
                inside = inside*-1
                cumilation = 0  
        #Side
        elif array[row][col] == 1 and array[row-1][col] == 1 and array[row+1][col] == 1:
            inside = inside*-1
        elif array[row][col] == 0 and inside == 1:
            insideCount += 1
            array[row][col] = 2
        if array[row][col] == 1:
            perimeterCount += 1

    
print(array)
print(insideCount)
print(perimeterCount)
print(perimeterCount+insideCount)

