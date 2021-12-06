
line = open('input', 'r').readline().split(",")
fish = [int(x) for x in line]

# naive solution, too slow for part 2
# for i in range(80):
#     new_fish = []
#     for i in range(len(fish)):
#         if fish[i] == 0:
#             new_fish.append(8)
#             fish[i] = 6
#         else:
#             fish[i] -= 1
#     fish.extend(new_fish)

fishies = {n: 0 for n in range(9)}

for f in fish:
    fishies[f] += 1

for i in range(256):
    zero = fishies[0]
    for n in range(8):
        fishies[n] = fishies[n + 1]
    fishies[8] = zero
    fishies[6] += zero

print(sum(fishies.values()))
