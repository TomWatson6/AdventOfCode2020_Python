import re

required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
eye_colour = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def validate_section(key, value):
    if key == "byr":
        if len(value) == 4 and 1920 <= int(value) <= 2002:
            return True
    if key == "iyr":
        if len(value) == 4 and 2010 <= int(value) <= 2020:
            return True
    if key == "eyr":
        if len(value) == 4 and 2020 <= int(value) <= 2030:
            return True
    if key == "hgt":
        if value.endswith("cm"):
            if 150 <= int(value[:-2]) <= 193:
                return True
        if value.endswith("in"):
            if 59 <= int(value[:-2]) <= 76:
                return True
    if key == "hcl":
        match = re.search(r'^#(?:[0-9a-fA-F]{1,2}){3}$', value)
        if match:
            return True
    if key == "ecl":
        if value in eye_colour:
            return True
    if key == "pid":
        if len(value) == 9:
            return True
    if key == "cid":
        return True
    
    return False

input = open("input.txt").read()

passports = [x.split("\n") for x in input.split("\n\n")]
#passports = [x.split(" ") for sublist in passports for x in sublist]

concat_passports = []

for passport in passports:
    new_passport = []
    for section in passport:
        new_section = section.split(" ")
        new_section = [x.split(":") for x in new_section]
        new_passport += new_section
    concat_passports.append(new_passport)

passports = concat_passports
filtered_passports = []
valid_passports = 0

for passport in passports:
    names = [x[0] for x in passport]
    found = True
    for section in required:
        if section not in names:
            found = False
            break
    if found:
        valid_passports += 1
        filtered_passports.append(passport)

print("Part 1:", valid_passports)

valid_passports = 0

for passport in filtered_passports:
    valid = True
    for section in passport:
        if not validate_section(section[0], section[1]):
            valid = False
            break
    if valid:
        valid_passports += 1

print("Part 2:", valid_passports)

