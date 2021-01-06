
def run(instructions):
    acc = 0

    visited = []
    x = 0

    found = False

    while x not in visited:

        if x >= len(instructions):
            found = True
            break

        visited.append(x)
        if instructions[x][0] == "acc":
            acc += instructions[x][1]
        if instructions[x][0] == "jmp":
            x += instructions[x][1]
            continue
        x += 1

    if found:
        print("Part 2:", acc)

    return acc


lines = open("input.txt").readlines()
lines = [x.replace("+", "").strip("\n") for x in lines]
instructions = [x.split(" ") for x in lines]
instructions = [[x[0], int(x[1])] for x in instructions]


acc = run(instructions)    

print("Part 1:", acc)

for instruction in instructions:
    modded = []

    if instruction[0] == "acc":
        continue
    elif instruction[0] == "jmp":
        instruction[0] = "nop"
    else:
        instruction[0] = "jmp"

    acc = run(instructions)

    if instruction[0] == "jmp":
        instruction[0] = "nop"
    else:
        instruction[0] = "jmp"
