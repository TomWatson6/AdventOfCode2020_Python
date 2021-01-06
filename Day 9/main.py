

numbers = open("input.txt").readlines()
numbers = [int(x) for x in numbers]

preamble = 25
found = False
part1 = 0

for x in range(preamble, len(numbers)):
    pre_numbers = dict.fromkeys(numbers[x - preamble:x])
    valid = False
    for num in pre_numbers:
        valid = False
        if (numbers[x] - num) in pre_numbers and num != numbers[x] - num:
            valid = True
            break
    if not valid:
        found = True
        part1 = numbers[x]
        break

print("Part 1:", part1)

part2 = 0
found = False

for x in range(len(numbers) - 1):
    num_list = []
    y = x
    while sum(num_list) < part1:
        num_list.append(numbers[y])

        if sum(num_list) == part1:
            part2 = min(num_list) + max(num_list)
            found = True
            break

        y += 1
    if found:
        break

print("Part 2:", part2)