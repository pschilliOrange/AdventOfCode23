lines = []
with open('Day3/input.txt', 'r') as file:
    lines.append('.'*142)
    for line in file:
        lines.append('.' + line.strip() + '.')
    lines.append('.'*142)
sum = 0
for i in range(0,142):
    for j in range(0,142):
        if lines[i][j] == '*':
            alreadyChecked = []
            numbers = []
            for l in range(i-1,i+2):
                for m in range(j-1,j+2):
                    if lines[l][m].isdigit() and (l,m) not in alreadyChecked:
                        alreadyChecked.append((l,m))
                        counter = 1
                        while lines[l][m-counter].isdigit():
                            alreadyChecked.append((l,m-counter))
                            counter += 1
                        startNum = m - counter + 1
                        counter = 1
                        while lines[l][m+counter].isdigit():
                            alreadyChecked.append((l,m+counter))
                            counter += 1
                        endNum = m + counter - 1
                        num = int(str(lines[l][startNum:endNum+1]))
                        numbers.append(num)
            if len(numbers) == 2:
                sum += numbers[0]*numbers[1]
print(sum)
