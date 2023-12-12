import numpy as np
with open('Day3/input.txt', 'r') as file:
    content = file.read()

# Splitting the content into lines
lines = content.splitlines()
N = len(lines)
M = len(lines[0])
matrix = np.zeros((N,M))
# Get matrix with 1's where there is a symbol adjacent
for i in range(0,N):
    for j in range(0,M):
         if lines[i][j] != '.' and not lines[i][j].isdigit():
            matrix[i,j] = 1
            matrix[min(i+1, N-1),j] = 1
            matrix[max(i-1, 0), j] = 1
            matrix[i, min(j+1, M-1)] = 1
            matrix[i, max(j-1, 0)] = 1
            matrix[min(i+1, N-1), min(j+1, M-1)] = 1
            matrix[max(i-1, 0), min(j+1, M-1)] = 1
            matrix[min(i+1, N-1), max(j-1, 0)] = 1
            matrix[max(i-1, 0), max(j-1, 0)] = 1
digits = []
adjacent = 0
num_sum = 0
for i in range(0,N):
    for j in range(0,M):
        if lines[i][j].isdigit():
            digits.append(lines[i][j])
            if matrix[i,j] == 1:
                adjacent = 1
            if j == M-1 or not lines[i][j+1].isdigit():
                if adjacent == 1:
                    num = int(''.join(digits))
                    num_sum += num
                adjacent = 0
                digits = []
print(num_sum)