from typing import Dict, Set, Tuple
import itertools


lines = open('input', 'r').readlines()
coords = [[int(i) for i in list(line.strip())] for line in lines]
coords_map = {}
for i in range(len(coords)):
    for j in range(len(coords[i])):
        coords_map[i, j] = coords[i][j]

total_flashes = 0


def produce_new_coords(curr):
    acc = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            if i == 0 and j == 0:
                continue
            acc.append((add_tuple(curr, (i, j))))
    return acc


def add_tuple(t1, t2):
    return tuple(map(sum, zip(t1, t2)))


def print_coords(coords_map, count):
    fin_string = ''
    for i in range(count):
        for j in range(count):
            fin_string += str(coords_map[i, j])
        fin_string += '\n'
    print(fin_string)


def perform_flash(d: Dict[Tuple[int, int], int]):
    global total_flashes

    def perform_flash_acc(d: Dict[Tuple[int, int], int], curr: Tuple[int, int]) -> Dict[Tuple[int, int], int]:
        if curr not in d.keys() or d[curr] == 0:
            return d
        d[curr] += 1
        if d[curr] > 9:
            d[curr] = 0
            for c in produce_new_coords(curr):
                d = perform_flash_acc(d, c)
        return d

    d = {k: v + 1 for k, v in d.items()}
    to_flash = set()
    for k, v in d.items():
        if v > 9:
            to_flash.add(k)
    for flash in to_flash:
        d = perform_flash_acc(d, flash)
    total_flashes += list(d.values()).count(0)
    return d


for i in range(1000):
    coords_map = perform_flash(coords_map)
    if all(v == 0 for v in coords_map.values()):
        print(i + 1)
        break

print(total_flashes)
