import numpy as np
with open('Day4/input.txt', 'r') as file:
    content = file.read()
# Splitting the content into lines
lines = content.splitlines()
sum = 0
for line in lines:
    line = line.split(':')[1]
    winning = line.split('|')[0].strip().split(' ')
    yours  = line.split('|')[1].strip().split(' ')
    winning = [elem for elem in winning if elem != '']
    yours = [elem for elem in yours if elem != '']
    matching = [elem for elem in yours if elem in winning]
    print(matching)
    if len(matching) >= 1:
        sum += 2**(len(matching)-1)

    

print(sum)
