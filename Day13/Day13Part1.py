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
        symFound = True
        for symInd in range(min(rowInd, len(pattern)-rowInd)):
            if pattern[rowInd - 1 - symInd] != pattern[rowInd + symInd]:
                symFound = False 
                break
        if symFound == True:
            rowsAbove = rowInd
            break
    print('   ')
    print(pattern)
    print(len(pattern))
    if symFound == True:
        if rowsAbove >= len(pattern):
            print()
            print(rowsAbove)
        totalSum += rowsAbove*100
        continue

    #checkColumns
    for colInd in range(1, len(pattern[0])):
        symFound = True
        for symInd in range(min(colInd, len(pattern[0])-colInd)):
            colAbove = [pattern[lineInd][colInd - symInd - 1] for lineInd in range(len(pattern))]
            colBelow = [pattern[lineInd][colInd + symInd] for lineInd in range(len(pattern))]
            if colAbove != colBelow:
                symFound = False
                break
        if symFound == True:
            colsLeft = colInd
            break
    if symFound == True:
        totalSum += colsLeft
        print(colsLeft)
        continue
print(totalSum)