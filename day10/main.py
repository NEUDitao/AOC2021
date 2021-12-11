
from typing import List, Union


lines = [list(l.strip()) for l in open('input', 'r').readlines()]

points = {')': 3, ']': 57, '}': 1197, '>': 25137}
auto_points = {'(': 1, '[': 2, '{': 3, '<': 4}
open_to_close = {"{": "}", "(": ")", "[": "]", "<": ">"}
openers = open_to_close.keys()

autocomplete_scores: List[int] = []

final_score = 0

for line in lines:
    stack = []
    for c in line:
        if c in openers:
            stack.append(c)
        elif c != open_to_close[stack.pop()]:
            final_score += points[c]
            stack = []
            break
    if len(stack):
        autocomplete_score = 0
        for c in reversed(stack):
            autocomplete_score = ((5 * autocomplete_score) +
                                  auto_points[c])
        autocomplete_scores.append(autocomplete_score)

print(final_score)
print(sorted(autocomplete_scores)[(len(autocomplete_scores) - 1)//2])
