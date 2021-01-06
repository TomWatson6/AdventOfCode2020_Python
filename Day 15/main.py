
def shuffle_indexes(index, history):
    history[0] = history[1]
    history[1] = index
    return history

def append_number(number, numbers, records, index):
    history = records.get(number)
    if history != None:
        if len(history) == 1:
            records[number].append(index)
        else:
            records[number] = shuffle_indexes(index, history)
    else:
        records[number] = [index]

def play_game(input_path, target):
    f = open(input_path)
    input = f.read()
    numbers = [int(x) for x in input.split(",")]
    f.close()
    records = dict.fromkeys(numbers)

    for x in range(len(numbers)):
        records[numbers[x]] = [x]

    for x in range(len(numbers) - 1, target - 1):
        curr = numbers[x]
        history = records[curr]
        if len(history) == 1:
            numbers.append(0)
            append_number(0, numbers, records, x + 1)
        else:
            number = history[1] - history[0]
            numbers.append(number)
            append_number(number, numbers, records, x + 1)

    return numbers[-1]

input_path = "input.txt"

output = play_game(input_path, 2020)

print("Part 1:", output)

output = play_game(input_path, 30000000)

print("Part 2:", output)
