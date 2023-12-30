from functools import cache
with open('Day12/input.txt', 'r') as file:
    lines = file.readlines()

# def check(line, nums):
#     hashtagCount = 0
#     groups = []
#     for char in line:
#         if char == '.':
#             if hashtagCount != 0:
#                 groups.append(str(hashtagCount))
#                 hashtagCount = 0
#         else:
#             hashtagCount += 1
#     if line[-1] == '#':
#         groups.append(str(hashtagCount))
#     if groups == nums:
#         return True
#     else: 
#         return False
def getConsecutiveHashesFromStart(numlessLine):
    count = 0
    while count < len(numlessLine) and numlessLine[count] == '#':
        count += 1
    return count
def getConsecutiveQsOrHashesFromStart(numlessLine):
    dotCount = 0
    while dotCount < len(numlessLine) and numlessLine[dotCount] == '.':
        dotCount += 1
    count = dotCount
    while count < len(numlessLine) and (numlessLine[count] == '?' or numlessLine[count] == '#'):
        count += 1
    return count
@cache
def check_ways(numlessLine, nums):
    # print(numlessLine)
    # print(nums)
    # print()
    maxNextPosGroup = getConsecutiveQsOrHashesFromStart(numlessLine)
    if (nums == [] and '#' not in numlessLine) or (numlessLine == '' and nums[0] == 0 and len(nums) == 1):
        return 1
    elif (nums[0] == 0 and len(nums) == 1 and '#' in numlessLine) or (numlessLine == '' and nums[0] != 0) or (numlessLine == '' and len(nums) != 1):
        return 0
    print(nums)
    if maxNextPosGroup < int(nums[0]):
        return 0
    if numlessLine[0] == '.':
        if nums[0] == 0:
            nums = nums[1:]
        totalSum = check_ways(numlessLine[1:], nums)
    elif numlessLine[0] == '#':
        consecHashes = getConsecutiveQsOrHashesFromStart(numlessLine)
        if nums[0] == 0:
            return 0
        elif nums[0] >= 1:
            nums = tuple([nums[0] - 1, nums[1:]])
        totalSum = check_ways(str(numlessLine[1:]), nums)
    elif numlessLine[0] == '?':
        if nums[0] == 0:
            nums = tuple(nums[1:])
            totalSum = check_ways(numlessLine[1:], nums)
        else:
            hashtagNums = list(nums)
            consecQs = getConsecutiveQsOrHashesFromStart(numlessLine)
            if consecQs >= hashtagNums[0]:
                temp = hashtagNums[0]
                hashtagNums[0] = 0
                withHashes = check_ways(numlessLine[temp:], hashtagNums)
            else:
                withHashes = 0
            withoutHashes = check_ways(numlessLine[1:], nums)
            # print(numlessLine[1:])
            # print(withoutHashes, '*')
            # print(nums)
            # print(withHashes, '*')
            # print(hashtagNums)
            # print()
            totalSum = withHashes + withoutHashes
    return totalSum


totalSum = 0
for line in lines:
    line = line 
    lineSum = 0
    numlessLine = line.split(' ')[0]
    numlessLine = numlessLine + ('?' + numlessLine)*4
    nums = line.split(' ')[1].strip().split(',')*5
    for i in range(len(nums)):
        nums[i] = int(nums[i])
    print(numlessLine)
    print(nums)
    lineSum = check_ways(numlessLine, tuple(nums))
    totalSum += lineSum
    print(lineSum)
print(totalSum)