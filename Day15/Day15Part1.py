with open('Day15/input.txt', 'r') as file:
    line = file.readlines()[0]
strings = [string.strip() for string in line.split(',')]
totSum = 0
for string in strings:
    currValue = 0
    for char in string:
        currValue += ord(char)
        currValue = currValue*17
        currValue = currValue % 256
    totSum += currValue
print(totSum)
