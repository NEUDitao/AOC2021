
from typing import Dict, List, Optional


lines = open('input', 'r').readlines()

graph: Dict[str, List[str]] = {}
for line in lines:
    start, end = line.strip().split('-')
    graph[start] = graph.get(start, []) + [end]
    graph[end] = graph.get(end, []) + [start]


def find_path(start: str, seen: List[str], dup: Optional[str]) -> int:
    global graph
    if start == 'end':
        return 1
    if start == 'start' and 'start' in seen:
        return 0
    if start.islower() and start in seen:
        if not dup:
            dup = start
        else:
            return 0
    seen = seen + [start]
    graph_sum = 0
    for node in graph[start]:
        graph_sum += find_path(node, seen, dup)
    return graph_sum


print(find_path('start', [], None))
