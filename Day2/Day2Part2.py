with open('Day2/input.txt', 'r') as file:
    content = file.read()

# Splitting the content into lines
lines = content.splitlines()
game = 1
game_sum = 0
for line in lines:
    green_max = 0
    red_max = 0
    blue_max = 0
    sets = line.split(':')[1].split(';')
    for set in sets:
        colors = set.split(',')
        for color in colors:
            if color[-5:] == 'green':
                green = int(''.join([char for char in color if char.isdigit()]))
                if green > green_max:
                    green_max = green
            elif color[-4:] == 'blue':
                blue = int(''.join([char for char in color if char.isdigit()]))
                if blue > blue_max:
                    blue_max = blue
            elif color[-3:] == 'red':
                red = int(''.join([char for char in color if char.isdigit()]))
                if red > red_max:
                    red_max = red
            else:
                print('ERRROOOORRR')
                break
    game_sum += green_max*red_max*blue_max
print(game_sum)