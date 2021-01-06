
def get_adjacents(chairs, coord):
    adjacents = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            adjacent = [coord[0] + y, coord[1] + x]
            valid = True
            if adjacent[0] < 0 or adjacent[0] >= height:
                valid = False
            if adjacent[1] < 0 or adjacent[1] >= width:
                valid = False
            if valid:
                adjacents.append(adjacent)
    adjacents = [chairs[x[0]][x[1]] for x in adjacents]

    return adjacents

def get_seen_adjacents(chairs, coord):
    adjacents = []

    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            adjacent = coord
            valid = True
            while chairs[adjacent[0]][adjacent[1]] == '.' or adjacent == coord:
                adjacent = [adjacent[0] + y, adjacent[1] + x]
                if adjacent[0] < 0 or adjacent[0] >= height:
                    valid = False
                    break
                if adjacent[1] < 0 or adjacent[1] >= width:
                    valid = False
                    break
            
            if valid:
                adjacents.append(adjacent)
    adjacents = [chairs[x[0]][x[1]] for x in adjacents]

    return adjacents

chairs = open("input.txt").readlines()
chairs = [[char for char in x.strip("\n")] for x in chairs]

width = len(chairs[0])
height = len(chairs)

new_chairs = []
iterations = 0

while True:
    new_chairs = []

    for y in range(height):
        new_row = []
        for x in range(width):
            adjacents = get_adjacents(chairs, [y, x])
            if chairs[y][x] == 'L' and not '#' in adjacents:
                new_row.append('#')
            elif chairs[y][x] == '#' and len([x for x in adjacents if x == '#']) >= 4:
                new_row.append('L')
            else:
                new_row.append(chairs[y][x])
        new_chairs.append(new_row)
    iterations += 1

    if chairs == new_chairs:
        break
    else:
        chairs = new_chairs

flattened_chairs = [x for sublist in chairs for x in sublist]
print("Part 1:", len([x for x in flattened_chairs if x == '#']))
print("Iterations:", iterations)
iterations = 0

chairs = open("input.txt").readlines()
chairs = [[char for char in x.strip("\n")] for x in chairs]

while True:
    new_chairs = []

    for y in range(height):
        new_row = []
        for x in range(width):
            adjacents = get_seen_adjacents(chairs, [y, x])
            if chairs[y][x] == 'L' and not '#' in adjacents:
                new_row.append('#')
            elif chairs[y][x] == '#' and len([x for x in adjacents if x == '#']) >= 5:
                new_row.append('L')
            else:
                new_row.append(chairs[y][x])
        new_chairs.append(new_row)
    iterations += 1

    if chairs == new_chairs:
        break
    else:
        chairs = new_chairs

flattened_chairs = [x for sublist in chairs for x in sublist]
print("Part 2:", len([x for x in flattened_chairs if x == '#']))
print("Iterations:", iterations)