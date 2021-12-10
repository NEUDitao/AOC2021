

from math import prod
from typing import Dict, Set, Tuple


lines = open('input', 'r').readlines()

coords = [[int(i) for i in list(line.strip())] for line in lines]

risk_level = 0
coords_map = {}
for i in range(len(coords)):
    for j in range(len(coords[i])):
        coords_map[i, j] = coords[i][j]


def is_low_point(coord: int, i: int, j: int,
                 coords_map: Dict[Tuple[int, int], int]) -> bool:
    return (coord < coords_map.get((i-1, j), 10)
            and coord < coords_map.get((i, j+1), 10)
            and coord < coords_map.get((i, j-1), 10)
            and coord < coords_map.get((i+1, j), 10))


def find_basin_size(prev_point: int, i: int, j: int,
                    coords_map: Dict[Tuple[int, int], int]) -> int:
    coord = coords_map.get((i, j), 9)
    if coord == 9:
        return 0
    elif coord > prev_point:
        coords_map.pop((i, j))
        return (1 + find_basin_size(coord, i+1, j, coords_map)
                + find_basin_size(
            coord, i-1, j, coords_map)
            + find_basin_size(
            coord, i, j+1, coords_map)
            + find_basin_size(
            coord, i, j-1, coords_map))
    else:
        return 0


# part 1
for i in range(len(coords)):
    for j in range(len(coords[i])):
        coord = coords_map[i, j]
        if is_low_point(coord, i, j, coords_map):
            risk_level += (coord + 1)

print(risk_level)

# part 2
sizes = []

for i in range(len(coords)):
    for j in range(len(coords[i])):
        coord = coords_map[i, j]
        if is_low_point(coord, i, j, coords_map):
            basin_size = find_basin_size(coord-1, i, j, coords_map.copy())
            sizes.append(basin_size)

sizes.sort()
print(sizes[-1] * sizes[-2] * sizes[-3])
