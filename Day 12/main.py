

def manhattan_distance(position):
    return abs(position[0]) + abs(position[1])

f = open("input.txt")
instructions = f.readlines()
f.close()
instructions = [[x[0], int(x[1:].strip("\n"))] for x in instructions]

position = [0, 0]

headings = ['E', 'S', 'W', 'N']

directions = dict.fromkeys(headings)
directions['E'] = [1, 0]
directions['S'] = [0, -1]
directions['W'] = [-1, 0]
directions['N'] = [0, 1]

direction = 0

for instruction in instructions:
    if instruction[0] in directions:
        position[0] = position[0] + (directions[instruction[0]][0] * instruction[1])
        position[1] = position[1] + (directions[instruction[0]][1] * instruction[1])
    else:
        if instruction[0] == 'L':
            direction -= instruction[1] // 90
        elif instruction[0] == 'R':
            direction += instruction[1] // 90
        else:
            key = headings[direction % len(directions)]
            position[0] = position[0] + (directions[key][0] * instruction[1])
            position[1] = position[1] + (directions[key][1] * instruction[1])

print("Part 1:", manhattan_distance(position))

position = [0, 0]
waypoint = [10, 1]
direction = 0

def rotate(position, waypoint, instruction):
    if instruction[0] == 'L':
        instruction[0] = 'R'
        instruction[1] = 360 - instruction[1]

    relative_waypoint = [waypoint[0] - position[0], waypoint[1] - position[1]]
    post_rotation_translation = [waypoint[0] - relative_waypoint[0], waypoint[1] - relative_waypoint[1]]

    for _ in range(instruction[1] // 90):
        relative_waypoint = [relative_waypoint[1], -relative_waypoint[0]]

    waypoint[0] = relative_waypoint[0] + post_rotation_translation[0]
    waypoint[1] = relative_waypoint[1] + post_rotation_translation[1]

def translate(position, waypoint, magnitude):
    relative_waypoint = [waypoint[0] - position[0], waypoint[1] - position[1]]

    waypoint[0] += relative_waypoint[0] * magnitude
    waypoint[1] += relative_waypoint[1] * magnitude

    position[0] += relative_waypoint[0] * magnitude
    position[1] += relative_waypoint[1] * magnitude

for instruction in instructions:
    if instruction[0] in directions:
        waypoint[0] = waypoint[0] + (directions[instruction[0]][0] * instruction[1])
        waypoint[1] = waypoint[1] + (directions[instruction[0]][1] * instruction[1])
    elif instruction[0] in ['L', 'R']:
        rotate(position, waypoint, instruction)
    else:
        translate(position, waypoint, instruction[1])

print("Part 2:", manhattan_distance(position))