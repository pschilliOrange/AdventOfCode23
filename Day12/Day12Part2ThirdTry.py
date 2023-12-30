with open('Day12/input.txt', 'r') as file:
    lines = file.readlines()
import copy

def consecHashtagsFromStart(line):
    hashCount = 0
    while line[hashCount] == '#':
        hashCount += 1
    return hashCount
def getConsecutiveQMarksAndHashesFromInd(numlessLine, startFromInd):
    count = 0
    Qind = startFromInd
    while numlessLine[Qind] == '?' or numlessLine[Qind] == '#':
        count += 1
        Qind += 1
    return count


def numPossibilities(line, nums):
    #print(line)
    #print(nums)
    if nums == [] and '#' not in line:
        return 1
    elif nums == [] and '#' in line:
        return 0
    elif line == '':
        return 0
    if line[0] == '#':
        numHashesAtStart = consecHashtagsFromStart(line)
        numQsImediatelyAfterHashes = getConsecutiveQMarksAndHashesFromInd(line, numHashesAtStart)
        if nums[0] < numHashesAtStart:
            return 0
        elif numHashesAtStart + numQsImediatelyAfterHashes < nums[0]:
            return 0
        elif line[nums[0]] == '.' or line[nums[0]] == '?':
            return numPossibilities(line[nums[0]+1:], nums[1:])
        else:
            return 0
    elif line[0] == '?':
        lineWithHash = '#' + line[1:]
        lineWithDot = '.' + line[1:]
        return numPossibilities(lineWithHash, nums) + numPossibilities(lineWithDot, nums)
    elif line[0] == '.':
        return numPossibilities(line[1:], nums)
    
totalSum = 0
for line in lines:
    lineSum = 0
    numlessLine = line.split(' ')[0]
    numlessLine = numlessLine + ('?' + numlessLine)*4 + '.'
    nums = [int(num) for num in line.split(' ')[1].strip().split(',')*5]
    totalSum += numPossibilities(numlessLine, nums)
    lineSum = numPossibilities(numlessLine, nums)
    print('lineSum', lineSum)
print(totalSum)