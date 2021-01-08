

def solve(expression):
    counter = 0
    sequence_operations = []

    while counter < len(expression):
        if expression[counter] == ' ':
            counter += 1
            continue
        elif expression[counter] == '(':
            end = counter + 1
            nesting_level = 1
            while nesting_level > 0:
                if expression[end] == '(':
                    nesting_level += 1
                elif expression[end] == ')':
                    nesting_level -= 1
                end += 1
            segment = expression[counter + 1:end - 1]
            sequence_operations.append(solve(segment))
            counter = end - 1
        elif expression[counter] == '+' or expression[counter] == '*':
            sequence_operations.append(expression[counter])
        else:
            sequence_operations.append(int(expression[counter]))

        counter += 1

    x = 0

    while x < len(sequence_operations):
        if sequence_operations[x] == '+' or sequence_operations[x] == '*':
            if sequence_operations[x] == '+':
                sequence_operations[x] = sequence_operations[x - 1] + sequence_operations[x + 1]
            else:
                sequence_operations[x] = sequence_operations[x - 1] * sequence_operations[x + 1]
                
            sequence_operations[x - 1] = ''
            sequence_operations[x + 1] = ''
            sequence_operations = [a for a in sequence_operations if a != '']

            x -= 1
            
        x += 1

    return sequence_operations[0]

def solve2(expression):
    counter = 0
    sequence_operations = []

    while counter < len(expression):
        if expression[counter] == ' ':
            counter += 1
            continue
        elif expression[counter] == '(':
            end = counter + 1
            nesting_level = 1
            while nesting_level > 0:
                if expression[end] == '(':
                    nesting_level += 1
                elif expression[end] == ')':
                    nesting_level -= 1
                end += 1
            segment = expression[counter + 1:end - 1]
            sequence_operations.append(solve2(segment))
            counter = end - 1
        elif expression[counter] == '+' or expression[counter] == '*':
            sequence_operations.append(expression[counter])
        else:
            sequence_operations.append(int(expression[counter]))

        counter += 1

    x = 0

    while x < len(sequence_operations):
        if sequence_operations[x] == '+':
            sequence_operations[x] = sequence_operations[x - 1] + sequence_operations[x + 1]
            sequence_operations[x - 1] = ''
            sequence_operations[x + 1] = ''
            sequence_operations = [a for a in sequence_operations if a != '']

            x -= 1
            
        x += 1

    x = 0

    while x < len(sequence_operations):
        if sequence_operations[x] == '*':
            sequence_operations[x] = sequence_operations[x - 1] * sequence_operations[x + 1]
            sequence_operations[x - 1] = ''
            sequence_operations[x + 1] = ''
            sequence_operations = [a for a in sequence_operations if a != '']

            x -= 1
            
        x += 1

    return sequence_operations[0]

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

total = 0

for expression in lines:
    solution = solve(expression)
    total += solution

print("Part 1:", total)

total = 0

for expression in lines:
    solution = solve2(expression)
    total += solution

print("Part 2:", total)

