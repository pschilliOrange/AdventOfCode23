with open('Day1/input.txt', 'r') as file:
    content = file.read()

# Splitting the content into lines
lines = content.splitlines()
num_dict = {
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
            }

# Iterating through each line
sum = 0
for line in lines:
    print(line)
    nums = []
    for i in range(0,len(line)):
        if line[i].isdigit():
            nums.append(int(line[i]))
        else:
            for key in num_dict.keys():
                if key == line[i-len(key)+1:i+1]:
                    nums.append(num_dict[key])
    print(nums)
    sum = sum + 10*nums[0] + nums[len(nums)-1]
print(sum)