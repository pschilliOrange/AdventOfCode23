import numpy as np
with open('Day4/input.txt', 'r') as file:
    content = file.read()
# Splitting the content into lines
lines = content.splitlines()
numOfCopiesToGo = [1]*len(lines)
sum = len(numOfCopiesToGo)
print(lines[0])
i=0
for line in lines:
    line = line.split(':')[1]
    winning = line.split('|')[0].strip().split(' ')
    yours  = line.split('|')[1].strip().split(' ')
    winning = [elem for elem in winning if elem != '']
    yours = [elem for elem in yours if elem != '']
    matching = [elem for elem in yours if elem in winning]
    print(i)
    print(numOfCopiesToGo[i])
    line = lines[i]
    print(lines[2])
    for j in range(1,len(matching) + 1):
        numOfCopiesToGo[j+i] += 1*numOfCopiesToGo[i]
        sum += 1*numOfCopiesToGo[i]
    i +=1
print(numOfCopiesToGo)
print(sum)
