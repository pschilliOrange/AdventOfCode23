with open('Day8/input.txt', 'r') as file:
    lines = file.readlines()
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
cont = True
key = 'AAA'
while cont:
    if key == 'ZZZ':
        cont = False
        break
    if instructInd >= len(instructions):
        instructInd = 0
    instruction = instructions[instructInd]
    next = network[key][instruction]
    key = next
    instructCount += 1
    instructInd += 1
    
print(instructCount)