
class Tile:
    def __init__(self, id, tile_input):
        self.id = int(id)
        tile_input = [x.strip() for x in tile_input.split("\n")]
        for t in range(len(tile_input)):
            tile_input[t] = [char for char in tile_input[t]]
        self.raw_tile = tile_input

        # The following stored a tuple (flips, rotations) for dynamic programming 
        self.stored_configurations = dict()
        self.stored_configurations[(0, 0)] = self.raw_tile
        self.current = (0, 0)

    def __str__(self):
        to_return = ""
        for y in range(len(self.raw_tile)):
            for x in range(len(self.raw_tile[0])):
                to_return += self.raw_tile[y][x]
            to_return += "\n"
        return to_return

    def left(self):
        edge = ""
        for x in range(len(self.raw_tile) - 1, -1, -1):
            edge += self.raw_tile[x][0]
        return edge

    def right(self):
        edge = ""
        for x in range(len(self.raw_tile)):
            edge += self.raw_tile[x][-1]
        return edge

    def top(self):
        edge = ""
        for x in range(len(self.raw_tile[0])):
            edge += self.raw_tile[0][x]
        return edge

    def bottom(self):
        edge = ""
        for x in range(len(self.raw_tile[0]) - 1, -1, -1):
            edge += self.raw_tile[-1][x]
        return edge

    def flip(self):
        # self.current = ((self.current[0] + 1) % 2, (4 - self.current[1]) % 4)
        # if self.stored_configurations.get(self.current) != None:
        #     self.raw_tile = self.stored_configurations[self.current]
        #     return

        for x in range(len(self.raw_tile)):
            self.raw_tile[x] = self.raw_tile[x][::-1]

        # self.stored_configurations[self.current] = self.raw_tile

    def rotate(self, turns):
        # if self.current[0] == 0:
        #     self.current = (self.current[0], (self.current[1] + 1) % 4)
        # else:
        #     self.current = (self.current[0], (self.current[1] - 1) % 4)
        # if self.stored_configurations.get(self.current) != None:
        #     self.raw_tile = self.stored_configurations[self.current]
        #     return

        for _ in range(turns):
            new_raw_tile = []
            for x in range(len(self.raw_tile[0])):
                row = []
                for y in range(len(self.raw_tile) - 1, -1, -1):
                    row.append(self.raw_tile[y][x])
                new_raw_tile.append(row)
            self.raw_tile = new_raw_tile

        # self.stored_configurations[self.current] = self.raw_tile

    def check(self, coord, tile, grid):
        to_check = [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]
        fits = True
        for coordinate in to_check:
            check_tile = grid.get(coordinate)
            if check_tile != None:
                if coordinate[0] > coord[0]:
                    if check_tile.left() != tile.right()[::-1]:
                        fits = False
                elif coordinate[0] < coord[0]:
                    if check_tile.right() != tile.left()[::-1]:
                        fits = False
                elif coordinate[1] > coord[1]:
                    if check_tile.bottom() != tile.top()[::-1]:
                        fits = False
                else:
                    if check_tile.top() != tile.bottom()[::-1]:
                        fits = False
        return fits
    
    def tesselates(self, grid, coord, tile):
        to_check = [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]
        found_coord = []
        for coordinate in to_check:
            if grid.get(coordinate) == None:
                placed = False
                for _ in range(2):
                    for _ in range(4):
                        if self.check(coordinate, tile, grid):
                            found_coord.append(coordinate)
                            placed = True
                            break
                        tile.rotate(1)
                    if placed:
                        break
                    tile.flip()
                if placed:
                    break
        if len(found_coord) == 0:
            return None
        elif len(found_coord) > 1:
            print("More than 1 possibility")

        return found_coord[0]

def flip(grid):
    for x in range(len(grid)):
        grid[x] = grid[x][::-1]
    return grid

def rotate(grid, turns):
    for _ in range(turns):
        new_grid = []
        for x in range(len(grid[0])):
            row = []
            for y in range(len(grid) - 1, -1, -1):
                row.append(grid[y][x])
            new_grid.append(row)
        grid = new_grid
    return grid

def print_grid(grid):
    f = open("output.txt", "w")

    ordering = []
    for coord in grid:
        ordering.append((coord[1], coord[0]))

    ordering.sort()

    while len(ordering) > 0:
        current_y = ordering[-1][0]
        snapshot = [x for x in ordering if x[0] == current_y]
        processing = [(x[1], x[0]) for x in ordering if x[0] == current_y]
        for y in range(len(grid[processing[0]].raw_tile)):
            for tile_coord in processing:
                f.write(''.join(grid[tile_coord].raw_tile[y]) + " ")
            f.write("\n")
        f.write("\n")
        ordering = [x for x in ordering if x not in snapshot]
    
    f.close()

def read_grid():
    f = open("output.txt")
    contents = f.read().split("\n\n")
    f.close()

    final = []

    for row in contents:
        r = row.split("\n")
        r = r[1:-1]
        for line in r:
            current = ""
            for x in range(len(line)):
                if x == 0 or x == len(line) - 1:
                    continue
                if line[x + 1] == " " or line[x - 1] == " " or line[x] == " ":
                    continue
                current += line[x]
            final.append(current)

    return final


f = open("input.txt")
input = f.read()
f.close()

tile_inputs = input.split("\n\n")
tiles = []

for tile in tile_inputs:
    split_tile = tile.split(":\n")
    tiles.append(Tile(split_tile[0].strip("Tile "), split_tile[1]))

grid = dict()

grid[(0, 0)] = tiles[0]
tiles = tiles[1:]
changed = True

while len(tiles) > 0 and changed:
    changed = False
    found = False
    for placed in grid:
        for tile in tiles:
            result = grid[placed].tesselates(grid, placed, tile)
            if result != None:
                grid[result] = tile
                print("Placed:", tile.id, "at", result)
                tiles.remove(tile)
                changed = True
                found = True
                break
        if found:
            break

# coords = []

# for loc in grid:
#     coords.append(loc)

# ids = []
# for loc in coords:
#     ids.append(grid[loc].id)

# coords.sort()
# for loc in coords:
#     print(loc, ":", grid[loc].id)

# missing = [x.id for x in tiles if x.id not in ids]
# print("Missing:", missing)
    
print_grid(grid)

corners = []
adjacents_map = dict()

for coord in grid:
    to_check = [(coord[0] - 1, coord[1]), (coord[0] + 1, coord[1]), (coord[0], coord[1] - 1), (coord[0], coord[1] + 1)]
    for coordinate in to_check:
        if grid.get(coordinate) != None:
            if adjacents_map.get(coord) != None:
                adjacents_map[coord] += 1
            else:
                adjacents_map[coord] = 1

for coord in adjacents_map:
    if adjacents_map[coord] == 2:
        corners.append(grid[coord].id)

product = 1

for tile_id in corners:
    product *= tile_id

print("Part 1:", product)

def find_sea_monsters(grid, sea_monster):
    sea_monsters = 0

    for y in range(len(grid) - len(sea_monster)):
        for x in range(len(grid[0]) - len(sea_monster[0])):
            section = grid[y:y + len(sea_monster)]
            for i in range(len(section)):
                section[i] = section[i][x:x + len(sea_monster[0])]
            matches = True
            for i in range(len(section)):
                for j in range(len(section[0])):
                    if sea_monster[i][j] == '#' and sea_monster[i][j] != section[i][j]:
                        matches = False
            if matches:
                sea_monsters += 1
    return sea_monsters

grid = read_grid()

f = open("sea_monster.txt")
sea_monster = [x.strip("\n") for x in f.readlines()]

sea_monsters = []

for _ in range(2):
    for _ in range(4):
        sea_monsters.append(find_sea_monsters(grid, sea_monster))
        grid = rotate(grid, 1)
    grid = flip(grid)

# print("Sea Monsters:", sea_monsters)

sea_monsters = [x for x in sea_monsters if x != 0][0]

roughness = 0

for row in grid:
    roughness += len([x for x in row if x == '#'])

roughness -= 15 * sea_monsters

print("Part 2:", roughness)