with open('Day9/input.txt', 'r') as file:
    content = file.read()
# Splitting the content into lines
lines = content.splitlines()
history = []
for line in lines:
    print(line)
    nonZero = 1
    lastNum = []
    list = line.split(' ')
    for i in range(0,len(list)):
        list[i] = int(list[i].strip())
    while nonZero:
        temp = []
        nonZero = False
        for i in range(0,len(list)-1):
            temp.append(list[i+1]-list[i])
            if temp[i] != 0:
                nonZero = True
        if nonZero is False:
            lastNum.append(list[0])
            altSum = 0
            for i in range(0,len(lastNum)):
                altSum += (-1)**i*lastNum[i]
            history.append(altSum)
        else:
            lastNum.append(list[0])
            list = temp
print(history)
hist_sum = sum(history)
print(hist_sum)
