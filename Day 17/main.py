def get_neighbours(position):
    neighbours = []
    for x in range(position[0] - 1, position[0] + 2):
        for y in range(position[1] - 1, position[1] + 2):
            for z in range(position[2] - 1, position[2] + 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                else:
                    neighbours.append((x, y, z))
    return neighbours

f = open("simple_input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

grid = dict()

for x in range(len(lines[0])):
    for y in range(len(lines)):
        grid[(x, y, 0)] = lines[y][x]

for _ in range(6):
    new_grid = dict()

    for cube in grid:
        neighbours = get_neighbours(cube)
        print(neighbours)