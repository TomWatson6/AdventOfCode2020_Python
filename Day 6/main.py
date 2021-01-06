

input = open("input.txt").read()
groups = input.split("\n\n")
split_groups = [x.split("\n") for x in groups]
# fully_parsed_groups = [[char for char in x] for x in [y for y in [z for z in split_groups]]]
flattened_groups = []

for x in range(len(split_groups)):
    for y in range(len(split_groups[x])):
        if len(split_groups[x][y]) > 1:
            split_groups[x][y] = [char for char in split_groups[x][y]]
    flattened_groups.append([x for sublist in split_groups[x] for x in sublist])

flattened_groups = [set(x) for x in flattened_groups]

print("Part 1:", sum([len(x) for x in flattened_groups]))


common_groups = []

for group in split_groups:
    common_groups.append([])
    for letter in group[0]:
        found = True
        for person in group:
            if letter not in person:
                found = False
                break
        if found:
            common_groups[0].append(letter)

common_group_sums = [len(x) for x in common_groups]

print("Part 2:", sum(common_group_sums))
