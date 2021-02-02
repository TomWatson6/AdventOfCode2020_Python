

f = open("input.txt")
keys = [int(x.strip()) for x in f.readlines()]
f.close()

loops = []
subject_number = 7

for key in keys:
    value = 1
    loop_size = 0
    while value != key:
        value *= subject_number
        value = value % 20201227
        loop_size += 1
    loops.append(loop_size)

encryption_keys = []

for t in range(len(loops)):
    value = 1
    subject_number = keys[1 - t]
    for _ in range(loops[t]):
        value *= subject_number
        value = value % 20201227
    encryption_keys.append(value)

assert encryption_keys[0] == encryption_keys[1]

print("Answer:", encryption_keys[0])