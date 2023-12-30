with open('Day13/input.txt', 'r') as file:
    lines = file.readlines()
patterns = []
lastInd = 0
for lineInd in range(len(lines)):
    line = lines[lineInd].strip()
    if line == '':
        patterns.append([line.strip() for line in lines[lastInd:lineInd]])
        lastInd = lineInd + 1
totalSum = 0
print(patterns)
for pattern in patterns:
    #checkRows
    for rowInd in range(1,len(pattern)):
        symFound = False
        numDifferences = 0
        for symInd in range(min(rowInd, len(pattern)-rowInd)):
            if pattern[rowInd - 1 - symInd] != pattern[rowInd + symInd]:
                for charInd in range(len(pattern[0])):
                    if  pattern[rowInd - 1 - symInd][charInd] != pattern[rowInd + symInd][charInd]:
                        numDifferences += 1
        if numDifferences == 1:
            symFound = True
            rowsAbove = rowInd
            break
    if symFound == True:
        totalSum += rowsAbove*100
        continue

    #checkColumns
    for colInd in range(1, len(pattern[0])):
        symFound = False
        numDifferences = 0
        for symInd in range(min(colInd, len(pattern[0])-colInd)):
            colAbove = [pattern[lineInd][colInd - symInd - 1] for lineInd in range(len(pattern))]
            colBelow = [pattern[lineInd][colInd + symInd] for lineInd in range(len(pattern))]
            if colAbove != colBelow:
                for charInd in range(len(colAbove)):
                    if colAbove[charInd] != colBelow[charInd]:
                        numDifferences += 1
        if numDifferences == 1:
            symFound = True
            colsLeft = colInd
            break
    if symFound == True:
        totalSum += colsLeft
        continue
print(totalSum)