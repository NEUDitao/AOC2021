
f = open('./input', 'r')

lines = [int(line) for line in f.readlines()]

# part 1
prev_line = 99999999999999999999
acc = 0
for line in lines:
    acc += 1 if line > prev_line else 0
    prev_line = line

print('part 1:', acc)

# part 2

acc = 0

for i in range(2, len(lines) - 1):
    a = lines[i] + lines[i-1] + lines[i-2]
    b = lines[i-1] + lines[i] + lines[i+1]

    acc += 1 if b > a else 0

print('part 2:', acc)
