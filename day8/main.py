import itertools

lines = open('input', 'r').readlines()

acc = 0
for line in lines:
    numbers_map = {}
    (input_values, output_values) = line.split('|')

    next_input_values = []
    for i_val in input_values.strip().split():
        if len(i_val) == 2:
            numbers_map[1] = i_val
        elif len(i_val) == 4:
            numbers_map[4] = i_val
        elif len(i_val) == 3:
            numbers_map[7] = i_val
        elif len(i_val) == 7:
            numbers_map[8] = i_val
        else:
            next_input_values.append(i_val)
    five_len = [set(i) for i in next_input_values if len(i) == 5]
    six_len = [set(i) for i in next_input_values if len(i) == 6]

    # five_lens are 3, 2, and 5. 3 is the
    for i in range(len(five_len)):
        curr = five_len[i]
        others = five_len[:i] + five_len[i + 1:]
        if all([len(other - curr) == 1 for other in others]):
            numbers_map[3] = ''.join(curr)
            five_len = others
            break

    if len(five_len[0] - set(numbers_map[4])) == 2:
        numbers_map[5] = ''.join(five_len[0])
        numbers_map[2] = ''.join(five_len[1])
    else:
        numbers_map[2] = ''.join(five_len[0])
        numbers_map[5] = ''.join(five_len[1])

    # six_lens are 0, 6, and 9
    for digit in six_len:
        if len(digit - set(numbers_map[4])) == 2:
            numbers_map[9] = ''.join(digit)
        elif len(digit - set(numbers_map[5])) == 1:
            numbers_map[6] = ''.join(digit)
        else:
            numbers_map[0] = ''.join(digit)

    outputs = output_values.strip().split()

    final_str = ''
    for o in outputs:
        for num, perm in numbers_map.items():
            perms = itertools.permutations(perm)
            if tuple(o) in set(perms):
                final_str += str(num)
                break
    acc += int(final_str)

print(acc)
