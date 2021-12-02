
lines = open('input', 'r').readlines()

# part 1
horizontal = 0
vertical = 0

for line in lines:
    (direction, amt) = line.split()
    if direction == 'forward':
        horizontal += int(amt)
    elif direction == 'down':
        vertical += int(amt)
    elif direction == 'up':
        vertical -= int(amt)

print('part 1:', horizontal * vertical)

# part 2
horizontal = 0
vertical = 0
aim = 0

for line in lines:
    (direction, amt) = line.split()
    if direction == 'forward':
        horizontal += int(amt)
        vertical += aim * int(amt)
    elif direction == 'down':
        aim += int(amt)
    elif direction == 'up':
        aim -= int(amt)

print('part 2:', horizontal * vertical)
