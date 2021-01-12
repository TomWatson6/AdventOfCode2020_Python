import re

def check(rules, index, message, dictionary):
    rule = rules.get(index)
    dictionary["count"] += 1       

    for pos in rule:
        if type(pos) is str:
            dictionary["matched_message"] += pos
            break
        else:
            if index in pos:
                # pull matched message off of the message (if matched message doesn't exist, it won't pull anything off)
                # make temp pos by removing index from pos remembering it's position in pos??
                # expand outwards by making larger and larger string using starts with to check how many iterations
                #   match the beginning of the remainder of the message
                # make matched message = matched message + string established using size of it before it broke
                # break to check as normal with crazy string, should always be returning true??
                # temp = message[len(matched_message):]
                # dictionary["cyclic_matched_message"] = ""
                # temp_pos = [x for x in pos if x != index]
                # position = pos.index(index)
                # temp_to_add = str(to_add)
                # first = True
                # while temp.startswith(to_add):
                #     temp_to_add = dictionary["cyclic_matched_message"]
                #     if not first:
                #         if position > 0:
                #             temp_pos.insert(0, temp_pos[0])
                #         temp_pos.append(temp_pos[-1])
                #     match = True
                #     for i in pos:
                #         if not check(rules, i, message, dictionary):
                #             match = False
                #     if match or pos == rule[-1]:
                #         break
                #     else:
                #         dictionary["cyclic_matched_message"] = temp_to_add
                return True

            else:
                match = True
                matched_message_copy = dictionary["matched_message"]
                for i in pos:
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

# rules[8] = [[42], [42, 8]]
# rules[11] = [[42, 31], [42, 11, 31]]

# total = 0
# dictionary = dict()
# dictionary["count"] = 0

# for message in messages:
#     dictionary["matched_message"] = ""
#     if check(rules, 0, message, dictionary):
#         total += 1

# print("Part 2:", total)
# print("Number of checks:", dictionary["count"])