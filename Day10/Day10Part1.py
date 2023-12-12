with open('Day10/input.txt', 'r') as file:
    lines = file.readlines()
array = []
array.append('.'*(len(lines[0])+1))
for i in range(0,len(lines)):
    array.append('.' + lines[i] + '.')
    for j in range(0,len(lines[i])):
        if lines[i][j] == 'S':
            start = (i+1,j+1)
array.append('.'*(len(lines[0])+2))

dict = {start: 0}
visited = []
list = []
list.append(start)
visited.append(start)
def getAdjancencies(position):
    positions = []
    curr_letter = array[position[0]][position[1]]
    left = array[position[0]][position[1]-1]
    right = array[position[0]][position[1]+1]
    up = array[position[0]-1][position[1]]
    down = array[position[0]+1][position[1]]
    #check left
    if curr_letter in ['S', '-', '7', 'J']:
        if left in ['-', 'F', 'L']:
            positions.append(tuple([position[0], position[1]-1]))
    #check right
    if curr_letter in ['S', '-', 'F', 'L']:
        if right in ['-', '7', 'J']:
            positions.append(tuple([position[0], position[1]+1]))
    #check up
    if curr_letter in ['S', '|', 'L', 'J']:
        if up in ['|', '7', 'F']:
            positions.append(tuple([position[0]-1, position[1]]))
    #check down
    if curr_letter in ['S', '|', '7', 'F']:
        if down in ['|', 'L', 'J']:
            positions.append(tuple([position[0]+1, position[1]]))
    return positions
max = 0
while list:
    pos = list.pop(0)
    more_pos = getAdjancencies(pos)
    for i in range(len(more_pos)):
        if more_pos[i] not in visited:
            visited.append(more_pos[i])
            dict[more_pos[i]] = dict[pos] + 1
            if max < dict[more_pos[i]]:
                max = dict[more_pos[i]]
            list.append(more_pos[i])
print(max)
parity = -1
count = 0
cumilation = 0
for i in range(len(array)):
        for j in range(len(array[1])-1):
            if tuple([i,j]) in visited:
                if array[i][j] == '|':
                    parity = parity*(-1)
                elif array[i][j] in ['L', '7']:
                    cumilation += 1/2
                    if cumilation == 1:
                        parity = parity*(-1)
                        cumilation = 0
                elif array[i][j] in ['J', 'F']:
                    cumilation -= 1/2
                    if cumilation == -1:
                        parity = parity*(-1)
                        cumilation = 0
            elif parity == 1:
                count += 1
            elif cumilation != 0:
                print('error')
        if parity != -1:
            print('Error, parity off at end of line')
                
print(count)
            