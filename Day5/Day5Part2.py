import numpy as np
with open('Day5/input.txt', 'r') as file:
    content = file.read()
# Splitting the content into lines
lines = content.splitlines()
seedsWithSpaces = lines[0].split(':')[1].split(' ')
seeds =  [int(elem) for elem in seedsWithSpaces if elem != '']
seeds = [(seeds[i], seeds[i+1]) for i in range(0,len(seeds),2)]
notFound = True
#i = 8580000
while notFound:
    if i % 10000 == 0:
        print("current i:", i)
    currentNumbersSentToi = []
    currentNumbersSentToi.append(i)
    nextNumbersSentToi = []
    maybeNextNumbersSentToi = []
    previousLines = []
    for j in range(len(lines)-1,-1,-1):
        line = lines[j]
        if line[0:5] == "seeds":
            hits = []
            #print(currentNumbersSentToi)
            for num in currentNumbersSentToi:
                for seed in seeds:
                    if seed[0]<=num and num<seed[0]+seed[1]:
                        hits.append(num)
            if hits:
                #print(hits)
                answer = min(hits)
                notFound = False
                break
        if line == '':
            currentNumbersSentToi = currentNumbersSentToi + nextNumbersSentToi + maybeNextNumbersSentToi
            #print(currentNumbersSentToi)
            nextNumbersSentToi = []
            previousLines = []
            maybeNextNumbersSentToi = []
            continue
        if not line[0].isdigit():
            continue
        numsWithSpaces = []
        numsWithSpaces = line.split(' ')
        nums = []
        nums = [int(elem) for elem in numsWithSpaces if elem != '']
        listToRemove = []
        #print("Maybe", maybeNextNumbersSentToi)
        for p in range(len(maybeNextNumbersSentToi)-1,-1,-1):
            currNum = maybeNextNumbersSentToi[p]
            #print("currNum", currentNum)
            #print(line)
            if nums[1] <= currNum < nums[1]+nums[2]:
                maybeNextNumbersSentToi = [elem for elem in maybeNextNumbersSentToi if elem != currNum]
                #print("removed", maybeNextNumbersSentToi[p])
        #print("Maybe", maybeNextNumbersSentToi)
        for currentNum in currentNumbersSentToi:
            if nums[0] <= currentNum < nums[0]+nums[2]:
                nextNumbersSentToi.append(nums[1]+currentNum-nums[0])
                inOtherRange = 0
                for l in range(0,len(previousLines)):
                    OtherNums = previousLines[l]
                    if OtherNums[1] <= currentNum < OtherNums[1]+OtherNums[2]:
                        inOtherRange = 1
                if nums[1]<=currentNum<nums[1]+nums[2]:
                    inOtherRange = 1
                if inOtherRange == 0:
                    maybeNextNumbersSentToi.append(currentNum)
                currentNumbersSentToi = [elem for elem in currentNumbersSentToi if elem != currentNum]
        previousLines = previousLines + [nums]
    i += 1
    #notFound = False
print(answer)
print(i-1)
        