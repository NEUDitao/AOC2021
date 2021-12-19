from itertools import filterfalse
from collections import defaultdict
from math import inf as INFINITY
import heapq
import sys
from queue import PriorityQueue

f = [line.strip() for line in open('input', 'r').readlines()]

cave_map = {}

a = 1
n = (len(f) * 5) - 1

for x in range(n + 1):
    for y in range(n + 1):
        dist = (x // len(f)) + (y // len(f))
        new_val = int(f[x % len(f)][y % len(f)])
        for i in range(dist):
            new_val += 1
            if new_val > 9:
                new_val -= 9
        new_val += dist
        if new_val > 10:
            new_val = new_val % 9

        cave_map[x, y] = new_val

tentative_distance = defaultdict(lambda: sys.maxsize)
tentative_distance[0, 0] = 0


def neighbors(curr):
    x, y = curr
    neighbors = []
    if x + 1 <= n:
        neighbors.append((x+1, y))
    if y + 1 <= n:
        neighbors.append((x, y+1))
    if x - 1 >= 0:
        neighbors.append((x-1, y))
    if y - 1 >= 0:
        neighbors.append((x, y-1))
    return neighbors


def dijkstra(cave_map, tentative_distance, visited, to_visit):
    while to_visit:
        curr = to_visit[0]
        if curr in visited:
            to_visit = to_visit[1:]
            continue
        visited.add(curr)
        for neighbor in neighbors(curr):
            if neighbor in visited:
                continue
            added_distance = cave_map[neighbor] + tentative_distance[curr]
            if added_distance < tentative_distance[neighbor]:
                tentative_distance[neighbor] = added_distance
                to_visit.append(neighbor)

        if curr == (n, n):
            print(tentative_distance[n, n])
            return tentative_distance

    # return dijkstra(cave_map, tentative_distance, visited, to_visit[0], to_visit[1:])


res = dijkstra(cave_map, tentative_distance, set(), [(0, 0)])

# TODO: stolen dijkstra, need to figure out where my bug is... but to be frank I can't be arsed

inf = sys.argv[1] if len(sys.argv) > 1 else 'input'

ll = [[int(y) for y in x] for x in open(inf).read().strip().split('\n')]


def inr(pos, arr):
    return pos[0] in range(len(arr)) and pos[1] in range(len(arr[0]))


expanded = [[0 for x in range(5*len(ll[0]))] for y in range(5*len(ll))]

for x in range(len(expanded)):
    for y in range(len(expanded[0])):
        dist = x//len(ll) + y//len(ll[0])
        newval = ll[x % len(ll)][y % len(ll[0])]
        for i in range(dist):
            newval += 1
            if newval == 10:
                newval = 1
        expanded[x][y] = newval

ll = expanded

q = [(0, 0, 0)]
costs = {}
while True:
    cost, x, y = q[0]
    if x == len(ll)-1 and y == len(ll[0])-1:
        print(cost)
        break
    q = q[1:]
    for xx, yy in [(x+1, y), (x-1, y), (x, y-1), (x, y+1)]:
        if inr((xx, yy), ll):
            nc = cost + ll[xx][yy]
            if (xx, yy) in costs and costs[(xx, yy)] <= nc:
                continue
            costs[(xx, yy)] = nc
            q.append((nc, xx, yy))
    q = sorted(q)


