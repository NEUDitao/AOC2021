
from typing import Dict, List


lines = open('input', 'r').readlines()

graph: Dict[str, List[str]] = {}
for line in lines:
    start, end = line.strip().split('-')
    graph[start] = graph.get(start, []) + [end]
    graph[end] = graph.get(end, []) + [start]


def find_path(start: str, seen: List[str]) -> int:
    global graph
    if start == 'end':
        return 1
    else:
        next_nodes = graph[start]
        sum = 0
        for node in next_nodes:
            if node in seen:
                continue
            elif node.islower():
                sum += find_path(node, seen + [node])
            else:
                sum += find_path(node, seen)
        return sum


print(find_path('start', ['start']))
