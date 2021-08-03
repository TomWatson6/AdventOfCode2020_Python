

f = open("input.txt")
instructions = [x.strip() for x in f.readlines()]
f.close()

directions = {
    'nw': [-1, 1],
    'ne': [0, 1],
    'sw': [0, -1],
    'se': [1, -1],
    'w': [-1, 0],
    'e': [1, 0]
}

tiles = dict()

for x in range(len(instructions)):
    tile = [0, 0]
    for direction in directions:
        split = instructions[x].split(direction)
        magnitude = len(split) - 1
        instructions[x] = instructions[x].replace(direction, "")
        pos_change = directions[direction]
        tile = [tile[0] + (pos_change[0] * magnitude), tile[1] + (pos_change[1] * magnitude)]
    t = tuple(tile)
    if tiles.get(t) != None:
        tiles[t] += 1
    else:
        tiles[t] = 1

total = 0

for x in tiles:
    if tiles[x] % 2 == 1:
        total += 1

print("Part 1:", total)

def check(tile, tiles, new_tiles, is_adjacent):
    adjacents = [
        (tile[0] - 1, tile[1] + 1),
        (tile[0], tile[1] + 1),
        (tile[0], tile[1] - 1),
        (tile[0] + 1, tile[1] - 1),
        (tile[0] - 1, tile[1]),
        (tile[0] + 1, tile[1])
    ]
    
    if is_adjacent:
        if new_tiles.get(tile) == None:
            blacks = [x for x in adjacents if tiles.get(x) != None]
            blacks = [x for x in blacks if tiles[x] % 2 == 1]
            if len(blacks) == 2:
                new_tiles[tile] = 1
    else:
        blacks = [x for x in adjacents if tiles.get(x) != None]
        blacks = [x for x in blacks if tiles[x] % 2 == 1]
        if tiles[tile] % 2 == 1:
            if len(blacks) == 0 or len(blacks) > 2:
                new_tiles[tile] = tiles[tile] + 1
            else:
                new_tiles[tile] = tiles[tile]
        else:
            if len(blacks) == 2:
                new_tiles[tile] = tiles[tile] + 1
            else:
                new_tiles[tile] = tiles[tile]
        

for i in range(100):
    new_tiles = dict()
    for tile in tiles:
        check(tile, tiles, new_tiles, False)
        adjacents = [
            (tile[0] - 1, tile[1] + 1),
            (tile[0], tile[1] + 1),
            (tile[0], tile[1] - 1),
            (tile[0] + 1, tile[1] - 1),
            (tile[0] - 1, tile[1]),
            (tile[0] + 1, tile[1])
        ]
        for adj in adjacents:
            if new_tiles.get(adj) == None:
                check(adj, tiles, new_tiles, True)
    tiles = new_tiles
    blacks = [x for x in tiles if tiles.get(x) % 2 == 1]
    print("Iteration:", (i + 1), "/ Tile Count:", len(tiles), "/ Blacks:", len(blacks))

blacks = [x for x in tiles if tiles.get(x) % 2 == 1]

print("Part 2:", len(blacks))
