

input = open("input.txt").readlines()

numbers = [int(x) for x in input]
numbersDict = dict.fromkeys(numbers)

output = 0

for number in numbersDict:
    if(2020 - number) in numbersDict:
        output = number * (2020 - number)
        break

print("Part 1:", output)

for x in numbers:
    for y in numbers:
        for z in numbers:
            if x != y != z and x + y + z == 2020: 
                output = x * y * z

print("Part 2:", output)
