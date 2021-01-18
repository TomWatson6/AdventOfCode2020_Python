

f = open("input.txt")
lines = [x.strip() for x in f.readlines()]
f.close()

allergen_list = []
ingred_allergen_map = dict()
ingred_allergen_map_backup = dict()
allergen_ingred_map = dict()

for line in lines:
    split_line = [x.strip(")") for x in line.split(" (contains ")]
    ingreds = tuple(split_line[0].split(" "))
    allergens = split_line[1].split(", ")
    ingred_allergen_map[ingreds] = allergens
    ingred_allergen_map_backup[ingreds] = allergens
    for allergen in allergens:
        if allergen not in allergen_list:
            allergen_list.append(allergen)

count = 0
while len(allergen_list) > 0:
    containing = []
    current_allergen = allergen_list[count % len(allergen_list)]
    for ingreds in ingred_allergen_map:
        if current_allergen in ingred_allergen_map[ingreds]:
            containing.append(ingreds)
    common = []
    for contained in containing:
        if len(common) == 0:
            for c in contained:
                common.append(c)
        else:
            new_common = []
            for c in contained:
                if c in common:
                    new_common.append(c)
            common = new_common

    # print(common)
    if len(common) == 1:
        allergen_ingred_map[current_allergen] = common[0]
        allergen_list.remove(current_allergen)
        to_remove = []
        to_add = dict()
        for ingreds in ingred_allergen_map:
            new_ingreds = []
            for ingred in ingreds:
                if ingred != common[0]:
                    new_ingreds.append(ingred)
            alls = ingred_allergen_map[ingreds]
            new_ingreds_tuple = tuple(new_ingreds)
            if ingreds != new_ingreds_tuple:
                to_add[new_ingreds_tuple] = alls
                # ingred_allergen_map[new_ingreds_tuple] = alls
                to_remove.append(ingreds)
        for ingreds in to_remove:
            ingred_allergen_map.pop(ingreds)
        for ingreds in to_add:
            ingred_allergen_map[ingreds] = to_add[ingreds]
    count += 1

print(allergen_ingred_map)

allergen_matches = []
ingred_count = 0

for allerg in allergen_ingred_map:
    allergen_matches.append(allergen_ingred_map[allerg])

for ingreds in ingred_allergen_map:
    ingred_count += len(ingreds)

print("Part 1:", ingred_count)

allergen_tuples = []

for allerg in allergen_ingred_map:
    allergen_tuples.append((allerg, allergen_ingred_map[allerg]))

allergen_tuples.sort()

output = ""

for allerg in allergen_tuples:
    output += allergen_ingred_map[allerg[0]] + ","

output = output[:-1]

print("Part 2:", output)