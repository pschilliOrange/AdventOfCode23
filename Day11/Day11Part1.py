with open('Day11/input.txt', 'r') as file:
    lines = file.readlines()
universe = []
for lineInd in range(len(lines)):
    universe.append(list(lines[lineInd].strip()))
print(universe)
#Expand galazy
#Expand rows
insertedRows = 0
for rowInd in range(len(lines)-1, -1, -1):
    row = universe[rowInd]
    if '#' not in row:
        universe.insert(rowInd, ['.']*len(universe[0]))
        insertedRows += 1
#Expand columns
insertedCols = 0
for colInd in range(len(universe[0])-1, -1, -1):
    col = [universe[lineInd][colInd] for lineInd in range(len(universe))]
    #col = universe[:][colInd]
    print(col)
    if '#' not in col:
        for line in universe:
            line.insert(colInd, '.')
        insertedCols += 1
print('inserted rows', insertedRows)
print('inserted cols', insertedCols)

#find inds of galaxies
locations = []
for rowInd in range(len(universe)):
    for colInd in range(len(universe[0])):
        if universe[rowInd][colInd] == '#':
            locations.append([rowInd, colInd])
#Get distances
sumOfDistances = 0
for location1 in locations:
    rowInd1 = location1[0]
    colInd1 = location1[1]
    for location2 in locations:
        rowInd2 = location2[0]
        colInd2 = location2[1]
        if location1 == location2:
            continue
        sumOfDistances += abs(colInd1 - colInd2) + abs(rowInd1 - rowInd2)
print(sumOfDistances/2)
