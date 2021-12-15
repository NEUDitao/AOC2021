from collections import Counter, defaultdict
from typing import DefaultDict, Dict

f = open('input', 'r').readlines()

polymer = f[0].strip()
instrs = {}
for line in f[2:]:
    k, v = line.strip().split(' -> ')
    instrs[k] = v

# counts = Counter({(x + y): 1 for x, y in zip(polymer, polymer[1:])})
counts = Counter()
for (x, y) in zip(polymer, polymer[1:]):
    counts[x + y] += 1

for _ in range(40):
    new_counts = Counter()
    for k, v in counts.items():
        repl = instrs[k]
        (x, y) = tuple(k)
        new_counts[x + repl] += v
        new_counts[repl + y] += v
    counts = new_counts

# for _ in range(40):
#     new_polymer = ""
#     for i in range(len(polymer)):
#         poly = polymer[i:i+2]
#         repl = instrs.get(poly, None)
#         new_polymer += polymer[i]
#         if repl:
#             new_polymer += repl
#     polymer = new_polymer


# count = Counter(list(polymer.strip())).most_common()

# # count = Counter(counts).most_common()
dedup = Counter()
for k, v in counts.items():
    dedup[k[0]] += v
dedup[polymer[-1]] += 1

count = dedup.most_common()
# print(count)

most_common = count[0][1]
least_common = count[-1][1]


print(most_common - least_common)
