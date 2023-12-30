with open('Day21/input.txt', 'r') as file:
    lines = file.readlines()
garden = []
first = []
for i in range(134):
    first.append('#')
garden.append(first)
for line in lines:
    gardLine = []
    gardLine.append('#')
    for i in range(len(line)):
        gardLine.append(line[i])
    gardLine.append('#')
    garden.append(gardLine)
garden.append(first)

for row in range(len(garden)):
    for col in range(len(garden[0])):
        if garden[row][col] == 'S':
            startPos = [row, col]
            garden[row][col] = '.'
startPos = [66, 131]
def get_new_positions(pos):
    newPos = []
    if garden[pos[0]+1][pos[1]] == '.':
        newPos.append([pos[0]+1, pos[1]])
    if garden[pos[0]-1][pos[1]] == '.':
        newPos.append([pos[0]-1, pos[1]])
    if garden[pos[0]][pos[1]+1] == '.':
        newPos.append([pos[0], pos[1]+1])
    if garden[pos[0]][pos[1]-1] == '.':
        newPos.append([pos[0], pos[1]-1])
    return newPos
positions = []
lengths = []
positions.append(startPos)
for i in range(0,1000):
    newPos = []
    for pos in positions:
        list = get_new_positions(pos)
        for item in list:
            if item not in newPos:
                newPos.append(item)
    positions = []
    positions = newPos
    lengths.append(len(positions))
    print(i)
    print(len(positions))
    if i>= 2 and lengths[i] == lengths[i-2]:
        print(lengths)

print(len(positions))
