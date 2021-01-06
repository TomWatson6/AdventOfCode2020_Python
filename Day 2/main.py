

input = open("input.txt").readlines()

passwords = []

lines = [x.split(": ") for x in input]

for x in lines:
    x[0] = x[0].split(" ")
    char = x[0][1]
    bounds = x[0][0].split("-")
    lower = int(bounds[0])
    upper = int(bounds[1])
    password = x[1]
    passwords.append([lower, upper, char, password.strip("\n")])

valid_passwords = 0

for password in passwords:
    lower, upper = password[0:2]
    checksum = len([char for char in password[3] if char == password[2]])
    if checksum >= lower and checksum <= upper:
        valid_passwords += 1

print("Part 1:", valid_passwords)

valid_passwords = 0

for password in passwords:
    index1, index2 = password[0:2]
    if((password[3][index1 - 1] == password[2]) ^ (password[3][index2 - 1] == password[2])):
        valid_passwords += 1

print("Part 2:", valid_passwords)