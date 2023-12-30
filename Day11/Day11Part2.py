with open('Day11/input.txt', 'r') as file:
    lines = file.readlines()
universe = []
for lineInd in range(len(lines)):
    universe.append(list(lines[lineInd].strip()))
#Expand galazy
#Record empty row indices
emptyRows = []
for rowInd in range(len(lines)-1, -1, -1):
    row = universe[rowInd]
    if '#' not in row:
        emptyRows.append(rowInd)
#Record empty col indices
emptyCols = []
for colInd in range(len(universe[0])-1, -1, -1):
    col = [universe[lineInd][colInd] for lineInd in range(len(universe))]
    if '#' not in col:
        emptyCols.append(colInd)

#find inds of galaxies
locations = []
for rowInd in range(len(universe)):
    for colInd in range(len(universe[0])):
        if universe[rowInd][colInd] == '#':
            locations.append([rowInd, colInd])
#Get distances
multFactor = 1000000
sumOfDistances = 0
for location1 in locations:
    rowInd1 = location1[0]
    colInd1 = location1[1]
    for location2 in locations:
        rowInd2 = location2[0]
        colInd2 = location2[1]
        if location1 == location2:
            continue
        throughEmptyRows = 0
        for emptyRowInd in emptyRows:
            if (rowInd1 < emptyRowInd and emptyRowInd < rowInd2) or (rowInd2 < emptyRowInd and emptyRowInd < rowInd1):
                throughEmptyRows += 1
        throughEmptyCols = 0
        for emptyColInd in emptyCols:
            if (colInd1 < emptyColInd and emptyColInd < colInd2) or (colInd2 < emptyColInd and emptyColInd < colInd1):
                throughEmptyCols += 1

        sumOfDistances += abs(colInd1 - colInd2) + abs(rowInd1 - rowInd2) + (multFactor-1)*(throughEmptyCols+throughEmptyRows)
print(sumOfDistances/2)
