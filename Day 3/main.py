

lines = open("input.txt").readlines()
lines = [x.strip("\n") for x in lines]

increment_x = 3
increment_y = 1

current_x = 0
trees = 0

for x in range(0, len(lines), increment_y):
    if(lines[x][current_x % len(lines[x])] == '#'):
        trees += 1
    current_x += increment_x

print("Part 1:", trees)

increment_x = [1, 3, 5, 7, 1]
increment_y = [1, 1, 1, 1, 2]

tree_counts = []

for i in range(5):
    trees = 0
    current_x = 0
    for x in range(0, len(lines), increment_y[i]):
        if(lines[x][current_x % len(lines[x])] == '#'):
            trees += 1
        current_x += increment_x[i]
    tree_counts.append(trees)

product = 1

for count in tree_counts:
    product *= count

print("Part 2:", product)
    