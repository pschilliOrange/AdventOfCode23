with open('Day1/input.txt', 'r') as file:
    content = file.read()

# Splitting the content into lines
lines = content.splitlines()

# Iterating through each line
sum = 0
for line in lines:
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    sum = sum + 10*nums[0] + nums[len(nums)-1]
print(sum)