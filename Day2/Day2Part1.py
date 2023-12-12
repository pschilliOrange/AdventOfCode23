with open('Day2/input.txt', 'r') as file:
    content = file.read()

# Splitting the content into lines
lines = content.splitlines()
game = 1
game_sum = 0
for line in lines:
    possible = 1
    sets = line.split(':')[1].split(';')
    for set in sets:
        colors = set.split(',')
        for color in colors:
            if color[-5:] == 'green':
                green = int(''.join([char for char in color if char.isdigit()]))
                if green > 13:
                    possible = 0
                    break
            elif color[-4:] == 'blue':
                blue = int(''.join([char for char in color if char.isdigit()]))
                if blue > 14:
                    possible = 0
                    break
            elif color[-3:] == 'red':
                red = int(''.join([char for char in color if char.isdigit()]))
                if red > 12:
                    possible = 0
                    break
            else:
                print('ERRROOOORRR')
                break
    if possible == 1:
        game_sum += game
    game += 1
print(game_sum)