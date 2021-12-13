
from typing import List, Set, Tuple


lines = open('input', 'r').readlines()


def print_grid(dots: Set[Tuple[int, int]]):
    x_max = max(x for x, y in dots)
    y_max = max(y for x, y in dots)
    final_str = ''
    for y in range(y_max + 1):
        for x in range(x_max + 1):
            final_str += '#' if (x, y) in dots else '.'
        final_str += '\n'
    print(final_str)


dots = []
folds: List[Tuple[str, int]] = []
do_folds = False
for line in lines:
    if line == '\n':
        do_folds = True
    elif do_folds:
        split_line = line.split()
        axis, num = split_line[-1].split('=')
        folds.append((axis, int(num)))
    else:
        x, y = line.split(',')
        dots.append((int(x), int(y)))


# y = horizontal fold, x = vertical fold

for fold in folds:
    new_dots = set()
    axis, num = fold
    if axis == 'y':
        for dot in dots:
            if dot[1] > num:
                diff = dot[1] - num
                new_dot = (dot[0], num - diff)
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
    else:
        for dot in dots:
            if dot[0] > num:
                diff = dot[0] - num
                new_dot = (num - diff, dot[1])
                new_dots.add(new_dot)
            else:
                new_dots.add(dot)
    dots = new_dots

print_grid(dots)
