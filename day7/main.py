
positions = [int(x) for x in open('input', 'r').readline().split(',')]

min_position = min(positions)
max_position = max(positions)

lowest_cost = 9999999999999999999999999
index_of_lowest = 0
for index in range(min_position, max_position + 1):
    cost = 0
    for position in positions:
        distance = abs(position - index)
        for i in range(1, distance + 1):
            cost += i
    if cost < lowest_cost:
        lowest_cost = cost
        index_of_lowest = index

print(lowest_cost)
