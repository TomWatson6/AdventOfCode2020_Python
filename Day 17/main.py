

def output_grid(grid, x_bounds, y_bounds, z_bounds):
    for z in range(z_bounds[0], z_bounds[1] + 1):
        print()
        for y in range(y_bounds[0], y_bounds[1] + 1):
            print()
            for x in range(x_bounds[0], x_bounds[1] + 1):
                print(grid.get((x, y, z)), end="")

    print()
    print()

def output_grid2(grid, x_bounds, y_bounds, z_bounds, w_bounds):
    for w in range(w_bounds[0], w_bounds[1] + 1):
        for z in range(z_bounds[0], z_bounds[1] + 1):
            print()
            for y in range(y_bounds[0], y_bounds[1] + 1):
                print()
                for x in range(x_bounds[0], x_bounds[1] + 1):
                    print(grid.get((x, y, z, w)), end="")

    print()
    print()

def expand_grid(grid, x_bounds, y_bounds, z_bounds):
    x_bounds[0] -= 1
    x_bounds[1] += 1
    y_bounds[0] -= 1
    y_bounds[1] += 1
    z_bounds[0] -= 1
    z_bounds[1] += 1
    
    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            for z in range(z_bounds[0], z_bounds[1] + 1):
                if grid.get((x, y, z)) == None:
                    grid[(x, y, z)] = '.'

    #output_grid(grid, x_bounds, y_bounds, z_bounds)

def expand_grid2(grid, x_bounds, y_bounds, z_bounds, w_bounds):
    x_bounds[0] -= 1
    x_bounds[1] += 1
    y_bounds[0] -= 1
    y_bounds[1] += 1
    z_bounds[0] -= 1
    z_bounds[1] += 1
    w_bounds[0] -= 1
    w_bounds[1] += 1
    
    for x in range(x_bounds[0], x_bounds[1] + 1):
        for y in range(y_bounds[0], y_bounds[1] + 1):
            for z in range(z_bounds[0], z_bounds[1] + 1):
                for w in range(w_bounds[0], w_bounds[1] + 1):
                    if grid.get((x, y, z, w)) == None:
                        grid[(x, y, z, w)] = '.'

    num_cubes = x_bounds[1] - x_bounds[0] + 1
    num_cubes *= y_bounds[1] - y_bounds[0] + 1
    num_cubes *= z_bounds[1] - z_bounds[0] + 1
    num_cubes *= w_bounds[1] - w_bounds[0] + 1

    assert len(grid) == num_cubes

    #output_grid2(grid, x_bounds, y_bounds, z_bounds, w_bounds)

def get_neighbours(grid, position):
    neighbours = []
    for x in range(position[0] - 1, position[0] + 2):
        for y in range(position[1] - 1, position[1] + 2):
            for z in range(position[2] - 1, position[2] + 2):
                if x == 0 and y == 0 and z == 0:
                    continue
                else:
                    neighbour = grid.get((x, y, z))
                    if neighbour == None:
                        neighbours.append('.')
                        continue

                    neighbours.append(neighbour)
    return neighbours

def get_neighbours2(grid, position):
    neighbours = []
    for x in range(position[0] - 1, position[0] + 2):
        for y in range(position[1] - 1, position[1] + 2):
            for z in range(position[2] - 1, position[2] + 2):
                for w in range(position[3] - 1, position[3] + 2):
                    if x == 0 and y == 0 and z == 0 and w == 0:
                        continue
                    else:
                        neighbour = grid.get((x, y, z, w))
                        if neighbour == None:
                            neighbours.append('.')
                            continue

                        neighbours.append(neighbour)
    return neighbours

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

grid = dict()

dimensions_x = len(lines[0])
dimensions_y = len(lines)

for x in range(dimensions_x):
    for y in range(dimensions_y):
        grid[(x, y, 0)] = lines[y][x]

x_bounds = [0, dimensions_x - 1]
y_bounds = [0, dimensions_y - 1]
z_bounds = [0, 0]

for _ in range(6):
    expand_grid(grid, x_bounds, y_bounds, z_bounds)

    new_grid = dict()

    for cube in grid:
        neighbours = get_neighbours(grid, cube)
        active_neighbours = [x for x in neighbours if x == '#']

        if grid[cube] == '#':
            if 2 <= len(active_neighbours) <= 3:
                new_grid[cube] = '#'
            else:
                new_grid[cube] = '.'
        else:
            if len(active_neighbours) == 3:
                new_grid[cube] = '#'
            else:
                new_grid[cube] = '.'

    #output_grid(new_grid, x_bounds, y_bounds, z_bounds)

    grid = new_grid

    #output_grid(grid, x_bounds, y_bounds, z_bounds)

active_cubes = 0

for cube in grid:
    if grid[cube] == '#':
        active_cubes += 1

print("Part 1:", active_cubes)

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

grid = dict()

dimensions_x = len(lines[0])
dimensions_y = len(lines)

for x in range(dimensions_x):
    for y in range(dimensions_y):
        grid[(x, y, 0, 0)] = lines[y][x]

x_bounds = [0, dimensions_x - 1]
y_bounds = [0, dimensions_y - 1]
z_bounds = [0, 0]
w_bounds = [0, 0]

for _ in range(6):
    expand_grid2(grid, x_bounds, y_bounds, z_bounds, w_bounds)

    new_grid = dict()

    for cube in grid:
        neighbours = get_neighbours2(grid, cube)
        active_neighbours = [x for x in neighbours if x == '#']

        if grid[cube] == '#':
            if 2 <= len(active_neighbours) <= 3:
                new_grid[cube] = '#'
            else:
                new_grid[cube] = '.'
        else:
            if len(active_neighbours) == 3:
                new_grid[cube] = '#'
            else:
                new_grid[cube] = '.'

    #output_grid(new_grid, x_bounds, y_bounds, z_bounds)

    grid = new_grid

    active_cubes = 0

    for cube in grid:
        if grid[cube] == '#':
            active_cubes += 1

    print("Part 2:", active_cubes)

    #output_grid(grid, x_bounds, y_bounds, z_bounds)

active_cubes = 0

for cube in grid:
    if grid[cube] == '#':
        active_cubes += 1

print("Part 2:", active_cubes)