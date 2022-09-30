import time

input = open("input.txt").readlines()

numbers = [int(x) for x in input]
numbersDict = dict.fromkeys(numbers)

output = 0

start = time.time()

for number in numbersDict:
    if(2020 - number) in numbersDict:
        output = number * (2020 - number)
        break

end = time.time()

print("Part 1: {} in {:.3f} seconds".format(output, end - start))

start = time.time()

for i in range(len(numbers) - 2):
    for j in range(i, len(numbers) - 1):
        for k in range(j, len(numbers)):
            if numbers[i] + numbers[j] + numbers[k] == 2020:
                output = numbers[i] * numbers[j] * numbers[k]

end = time.time()

print("Part 2: {} in {:.3f} seconds".format(output, end - start))
