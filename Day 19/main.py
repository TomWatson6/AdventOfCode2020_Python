

def check(rules, index, message, dictionary):
    rule = rules.get(index)
    dictionary["count"] += 1
    match = True
    if len(dictionary["matched_message"]) >= len(message):
        return False
    for pos in rule:
        match = True
        if type(pos) is str:
            dictionary["matched_message"] += pos
        else:
            matched_message_copy = dictionary["matched_message"]
            for i in pos:
                if dictionary["matched_message"] == message and i != 31:
                    dictionary["matched_message"] += "c"
                if not check(rules, i, message, dictionary):
                    match = False

            if match or pos == rule[-1]:
                break
            else:
                dictionary["matched_message"] = matched_message_copy

    matched_message = dictionary["matched_message"]

    if len(matched_message) > 0:
        if message[0:len(matched_message)] == matched_message and index != 0:
            return True
        elif message == matched_message and index == 0:
            return True

    return False

f = open("input.txt")
input = f.read()
f.close()

sections = input.split("\n\n")

for x in range(len(sections)):
    sections[x] = [x for x in sections[x].split("\n")]
    for y in range(len(sections[x])):
        sections[x][y] = sections[x][y].strip()

rule_strings = sections[0]
messages = sections[1]

rules = dict()

for x in range(len(rule_strings)):
    left, right = rule_strings[x].split(": ")
    right = right.split(" | ")
    for y in range(len(right)):
        if right[y].startswith("\""):
            right[y] = right[y].strip("\"")
            break
        right[y] = [int(t) for t in right[y].split(" ")]

    rules[int(left)] = right

total = 0
dictionary = dict()
dictionary["count"] = 0

for message in messages:
    dictionary["matched_message"] = ""
    if check(rules, 0, message, dictionary):
        total += 1

print("Part 1:", total)
print("Number of checks:", dictionary["count"])

rules[8] = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]

total = 0
dictionary = dict()
dictionary["count"] = 0

for message in messages:
    dictionary["matched_message"] = ""
    if check(rules, 0, message, dictionary):
        total += 1

print("Part 2:", total)
print("Number of checks:", dictionary["count"])