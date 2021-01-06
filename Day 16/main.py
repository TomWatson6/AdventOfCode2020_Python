

f = open("input.txt")
input = f.read()
f.close()

sections = [x for x in input.split("\n\n")]

split_sections = [x.split("\n") for x in sections]

field_list = []
field_map = dict()

for line in split_sections[0]:
    divided = line.split(" ")
    end_of_field = 1
    for x in range(len(divided)):
        if divided[x].endswith(":"):
            divided[x] = divided[x].strip(":")
            end_of_field = x + 1
    field = divided[0:end_of_field]
    field = ' '.join(field)
    ranges = [x.split("-") for x in [divided[-3], divided[-1]]]
    for i in range(len(ranges)):
        ranges[i] = [int(x) for x in ranges[i]]
    field_map[field] = ranges
    field_list.append(field)

my_ticket = split_sections[1][1]
my_ticket = my_ticket.split(",")
my_ticket = [int(x) for x in my_ticket]

nearby_tickets = []

for line in split_sections[2][1:]:
    ticket = line.split(",")
    ticket = [int(x) for x in ticket]
    nearby_tickets.append(ticket)

def matches_ranges(number, ranges):
    for r in ranges:
        if r[0] <= number <= r[1]:
            return True
    return False

def valid_for_all_fields(number, field_map):
    for field in field_map:
        if matches_ranges(number, field_map[field]):
            return True
    return False

def is_valid(field, number, field_map):
    if matches_ranges(number, field_map[field]):
        return True
    else:
        return False

invalid_number_sum = 0
valid_tickets = [my_ticket]

for ticket in nearby_tickets:
    valid = True
    for number in ticket:
        if not valid_for_all_fields(number, field_map):
            invalid_number_sum += number
            valid = False
            break
    if valid:
        valid_tickets.append(ticket)

print("Part 1:", invalid_number_sum)

valid_maps = []

for t in range(len(valid_tickets)):
    ticket_mapping = []
    for n in range(len(valid_tickets[t])):
        valid_mapping = []
        for field in field_map:
            valid_mapping.append(is_valid(field, valid_tickets[t][n], field_map))
        ticket_mapping.append(valid_mapping)
    valid_maps.append(ticket_mapping)

validity_mapping = []

for index in range(len(field_map)):
    column_mapping = []
    for field in field_map:
        valid = []
        for ticket in valid_tickets:
            valid.append(is_valid(field, ticket[index], field_map))
        column_mapping.append(valid)
    validity_mapping.append([index, column_mapping])

column_possibilities = []

for x in range(len(validity_mapping)):
    possible_fields = []
    for y in range(len(validity_mapping[x][1])):
        if all(validity_mapping[x][1][y]):
            possible_fields.append(y)
    column_possibilities.append([x, possible_fields])

def len_inner(array):
    return len(array[1])

column_possibilities.sort(reverse=False, key=len_inner)

field_mapping = dict.fromkeys([x for x in field_map])

for x in range(len(column_possibilities)):
    if len(column_possibilities[x][1]) == 1:
        number = column_possibilities[x][1][0]
        field_mapping[field_list[number]] = column_possibilities[x][0]
        for p in column_possibilities:
            if number in p[1]:
                p[1].remove(number)

product = 1

for element in field_mapping:
    if element.startswith("departure"):
        product *= my_ticket[field_mapping[element]]

print("Part 2:", product)