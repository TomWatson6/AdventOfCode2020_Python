

f = open("input.txt")
numbers = f.read()
f.close()

numbers = [int(char) for char in numbers]

linked_numbers = dict()

for x in range(len(numbers)):
    prev = numbers[(x - 1) % len(numbers)]
    after = numbers[(x + 1) % len(numbers)]
    linked_numbers[numbers[x]] = [prev, after]

current = (numbers[0], linked_numbers[numbers[0]])
highest = max(numbers)

for _ in range(100):
    selected = current
    moving = []
    for _ in range(3):
        copy = []
        for c in linked_numbers[selected[1][1]]:
            copy.append(c)
        moving.append(selected[1][1])
        linked_numbers[selected[1][1]] = None
        selected = (selected[1][1], copy)
    selected = (selected[1][1], linked_numbers[selected[1][1]])

    linked_numbers[current[0]] = [current[1][0], selected[0]]
    linked_numbers[selected[0]] = [current[0], selected[1][1]]

    destination = (current[0] - 2) % len(numbers) + 1
    while linked_numbers[destination] == None:
        destination = (destination - 2) % len(numbers) + 1

    start = destination
    finish = linked_numbers[destination][1]

    for x in range(len(moving)):
        if x == 0:
            linked_numbers[moving[x]] = [start, moving[x + 1]]
        elif x == len(moving) - 1:
            linked_numbers[moving[x]] = [moving[x - 1], finish]
        else:
            linked_numbers[moving[x]] = [moving[x - 1], moving[x + 1]]
    linked_numbers[start] = [linked_numbers[start][0], moving[0]]
    linked_numbers[finish] = [moving[-1], linked_numbers[finish][1]]

    current = (linked_numbers[current[0]][1], linked_numbers[linked_numbers[current[0]][1]])

print("Part 1: ", end="")

current = linked_numbers[1][1]

for _ in range(len(numbers) - 1):
    print(current, end="")
    current = linked_numbers[current][1]

print()

linked_numbers = dict()

for x in range(len(numbers)):
    prev = numbers[(x - 1) % len(numbers)]
    after = numbers[(x + 1) % len(numbers)]
    linked_numbers[numbers[x]] = [prev, after]

prev = numbers[-1]
linked_numbers[prev] = [linked_numbers[prev][0], highest + 1]
linked_numbers[numbers[0]] = [1000000, linked_numbers[numbers[0]][1]]

for x in range(highest, 1000000, 1):
    after = (x + 2 % 1000000)
    linked_numbers[x + 1] = [prev, after]
    prev = (x + 1 % 1000000)

linked_numbers[1000000] = [linked_numbers[1000000][0], numbers[0]]

current = (numbers[0], linked_numbers[numbers[0]])

for _ in range(10000000):
    selected = current
    moving = []
    for _ in range(3):
        copy = []
        for c in linked_numbers[selected[1][1]]:
            copy.append(c)
        moving.append(selected[1][1])
        linked_numbers[selected[1][1]] = None
        selected = (selected[1][1], copy)
    selected = (selected[1][1], linked_numbers[selected[1][1]])

    linked_numbers[current[0]] = [current[1][0], selected[0]]
    linked_numbers[selected[0]] = [current[0], selected[1][1]]

    destination = (current[0] - 2) % 1000000 + 1
    while linked_numbers[destination] == None:
        destination = (destination - 2) % 1000000 + 1

    start = destination
    finish = linked_numbers[destination][1]

    for x in range(len(moving)):
        if x == 0:
            linked_numbers[moving[x]] = [start, moving[x + 1]]
        elif x == len(moving) - 1:
            linked_numbers[moving[x]] = [moving[x - 1], finish]
        else:
            linked_numbers[moving[x]] = [moving[x - 1], moving[x + 1]]
    linked_numbers[start] = [linked_numbers[start][0], moving[0]]
    linked_numbers[finish] = [moving[-1], linked_numbers[finish][1]]

    current = (linked_numbers[current[0]][1], linked_numbers[linked_numbers[current[0]][1]])

current = linked_numbers[1][1]

product = current * linked_numbers[current][1]

print("Part 2:", product)