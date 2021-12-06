
from typing import Dict, List, Tuple


raw_lines = open('input', 'r').readlines()
lines = [line.split(' -> ') for line in raw_lines]
coords = [([int(c) for c in line[0].split(',')],
           [int(c) for c in line[1].split(',')]) for line in lines]


def is_hetero(coord: Tuple[List[int], List[int]]):
    ((x1, y1), (x2, y2)) = coord
    return x1 == x2 or y1 == y2


def get_step(n1: int, n2: int):
    if n1 > n2:
        return -1
    else:
        return 1


coordinate_map: Dict[Tuple[int, int], int] = {}
for coord in coords:
    ((x1, y1), (x2, y2)) = coord
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            coordinate_map[(x1, i)] = coordinate_map.get((x1, i), 0) + 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            coordinate_map[(i, y1)] = coordinate_map.get((i, y1), 0) + 1
    else:
        for i in range(abs(x2 - x1) + 1):
            x = x1 + i * get_step(x1, x2)
            y = y1 + i * get_step(y1, y2)
            coordinate_map[x, y] = coordinate_map.get((x, y), 0) + 1

print(len([x for x in coordinate_map.values() if x > 1]))
