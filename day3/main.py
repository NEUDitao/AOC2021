
lines = open('input', 'r').readlines()

# part 1
gamma = []

for i in range(len(lines[0]) - 1):
    index_list = [line[i] for line in lines]
    gamma.append(max(index_list, key=index_list.count))

epsilon = ['1' if e == '0' else '0' for e in gamma]
gamma_binary = int(''.join(gamma), 2)
epsilon_binary = int(''.join(epsilon), 2)

print('part 1: gamma:', gamma_binary,
      'epsilon: ', epsilon_binary, 'power consumption: ', gamma_binary * epsilon_binary)

o2 = lines
co2 = lines
# part 2
for i in range(len(gamma)):
    column = [l[i] for l in o2]
    num_ones = column.count('1')
    num_zeroes = column.count('0')
    if num_ones >= num_zeroes:
        common = '1'
    else:
        common = '0'
    o2 = [line for line in o2 if line[i] != common]
    if len(o2) == 1:
        break

for i in range(len(epsilon)):
    column = [l[i] for l in co2]
    num_ones = column.count('1')
    num_zeroes = column.count('0')
    if num_ones < num_zeroes:
        uncommon = '1'
    else:
        uncommon = '0'
    co2 = [line for line in co2 if line[i] != uncommon]
    if len(co2) == 1:
        break

print(o2, co2)
o2_binary = int(o2[0], 2)
co2_binary = int(co2[0], 2)
print('part 2: o2:', o2_binary,
      'co2: ', co2_binary, 'power consumption: ', o2_binary * co2_binary)


def p2(codes):
    length = len(codes[0])

    oxygen = set(codes)
    for i in range(length):
        column = "".join(code[i] for code in oxygen)
        if column.count("0") <= column.count("1"):
            bit = "1"
        else:
            bit = "0"
        print(bit,
              column.count('1'), column.count('0'))

        oxygen = oxygen - set(code for code in oxygen if code[i] == bit)
        if len(oxygen) == 1:
            print(oxygen)
            oxygen = int(max(oxygen), 2)
            break

    co2 = set(codes)
    for i in range(length):
        column = "".join(code[i] for code in co2)
        if column.count("0") > column.count("1"):
            bit = "1"
        else:
            bit = "0"

        co2 = co2 - set(code for code in co2 if code[i] == bit)
        if len(co2) == 1:
            print(co2)
            co2 = int(max(co2), 2)
            break

    return oxygen * co2


print(p2(lines))
