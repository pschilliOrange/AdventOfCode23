with open('Day15/input.txt', 'r') as file:
    line = file.readlines()[0]
strings = [string.strip() for string in line.split(',')]
totSum = 0
boxes = {}
for string in strings:
    currValue = 0
    for charInd in range(len(string)):
        char = string[charInd]
        if char == '=':
            equalsSign = True
            if charInd + 1 < len(string):
                lenseNum = int(string[charInd+1:])
                print(lenseNum)
            else:
                lenseNum = 0
            lense = string[:charInd]
            break
        elif char == '-':
            equalsSign = False
            lenseNum = 0
            lense = string[:charInd]
            break
        currValue += ord(char)
        currValue = currValue*17
        currValue = currValue % 256
    if currValue in boxes:
        lenses = boxes[currValue]
        if equalsSign:
            lenses[lense] = lenseNum
        elif not equalsSign:
            if lense in lenses:
                del lenses[lense]
    else:
        lenses = {}
        if equalsSign:
            lenses[lense] = lenseNum
            boxes[currValue] = lenses
totSum = 0
for boxNum,lenses in boxes.items():
    lenseSlot = 1
    for lense,lenseNum in lenses.items():
        totSum += (boxNum + 1)*lenseSlot*lenseNum
        lenseSlot += 1
print(totSum)
print(boxes)