

def find_path(joltages, start, largest, stored_routes):
    count = 0
    inc = 0

    if start == largest:
        return 1
    
    for x in range(1, 4):
        if start + x in stored_routes:
            count += stored_routes.get(start + x)
        elif start + x in joltages:
            inc = find_path(joltages, start + x, largest, stored_routes)
            count += inc
            stored_routes[start + x] = inc

    return count

joltages = open("input.txt").readlines()
joltages = [int(x) for x in joltages]
joltages.sort()

jolt1 = 1
jolt3 = 1

for x in range(1, len(joltages)):
    diff = joltages[x] - joltages[x - 1]
    if diff == 1:
        jolt1 += 1
    elif diff == 3:
        jolt3 += 1

print("Part 1:", jolt1 * jolt3)

largest = max(joltages)
joltages = dict.fromkeys(joltages)
stored_routes = dict()

total = find_path(joltages, 0, largest, stored_routes)

print("Part 2:", total)