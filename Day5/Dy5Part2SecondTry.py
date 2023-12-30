import copy
with open('Day5/input.txt', 'r') as file:
    lines = file.readlines()
seedRanges = [int(num.strip()) for num in lines[0].split(':')[1].split(' ') if num != '']


max = 0
mappedRanges = []
finalRanges = []

for k in range(0, len(seedRanges), 2):
    startRange = seedRanges[k]
    endRange = seedRanges[k] + seedRanges[k+1] - 1
    length = endRange - startRange + 1
    sourceRanges = []
    sourceRanges.append([startRange, endRange])
    for i in range(2,len(lines)):
        poss = 0
        if len(sourceRanges) > 0 and sourceRanges[0][0] == 46 and sourceRanges[0][1] == 55:
            aaaa = 5
        for ran in sourceRanges:
            poss += ran[1] - ran[0] + 1
        for ran in mappedRanges:
            poss += ran[1] - ran[0] + 1
        if poss != length:
            print('uhoh')
        line = lines[i]
        if line == '':
            continue
        if not line[0].isdigit():
            temp = copy.deepcopy(sourceRanges)
            sourceRanges = []
            sourceRanges = temp + copy.deepcopy(mappedRanges)
            mappedRanges = []
            continue
        nums = [int(num.strip()) for num in line.split(' ') if num != '']
        destRanStart = nums[0] 
        destRanEnd = nums[0] + nums[2] - 1
        sourceRanStart = nums[1]
        sourceRanEnd = nums[1] + nums[2] - 1
        for j in range(len(sourceRanges)-1, -1, -1):
            sourceRange = sourceRanges[j]
            startRange = sourceRange[0]
            endRange = sourceRange[1]
            if startRange >= sourceRanStart and startRange <= sourceRanEnd and endRange > sourceRanEnd:
                newStartRange = sourceRanEnd + 1
                newEndRange = endRange
                lenMappedRange = sourceRanEnd - startRange + 1
                mappedRanges.append([destRanEnd - lenMappedRange + 1, destRanEnd])
                sourceRanges[j] = [newStartRange, newEndRange]
            elif startRange < sourceRanStart and endRange >= sourceRanStart and endRange <= sourceRanEnd:
                newStartRange = startRange
                newEndRange = sourceRanStart - 1
                lenMappedRange = endRange - sourceRanStart + 1
                mappedRanges.append([destRanStart, destRanStart + lenMappedRange - 1])
                sourceRanges[j] = [newStartRange, newEndRange]
            elif startRange >= sourceRanStart and endRange <= sourceRanEnd:
                lenMappedRange = endRange - startRange + 1
                lenNumsUnmappedInfront = startRange - sourceRanStart
                startMappedRange = destRanStart + lenNumsUnmappedInfront
                mappedRanges.append([startMappedRange, startMappedRange + lenMappedRange - 1])
                del sourceRanges[j]
            elif startRange <= sourceRanStart and endRange >= sourceRanEnd:
                #lenMappedRange = sourceRanEnd - sourceRanStart + 1 
                lenBottom = sourceRanStart - startRange 
                lenTop = endRange - sourceRanEnd
                mappedRanges.append([destRanStart, destRanEnd])
                del sourceRanges[j]
                if lenBottom > 0:
                    sourceRanges.append([startRange, startRange + lenBottom - 1])
                if lenTop > 0:
                    sourceRanges.append([sourceRanEnd + 1, sourceRanEnd + lenTop])
    finalRanges += sourceRanges
    poss = 0
min = 10000000000
for ran in finalRanges:
    poss += ran[1] - ran[0] + 1
    if min > ran[0]:
        min = ran[0]

print(min)