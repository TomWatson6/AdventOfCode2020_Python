
def contains_bag(bag_dictionary, colour, colour_to_check):
    contained_bags = bag_dictionary.get(colour)
    if contained_bags == None:
        return False
    else:
        if colour_to_check in [x[0] for x in contained_bags]:
            return True
        else:
            for bag in contained_bags:
                if(contains_bag(bag_dictionary, bag[0], colour_to_check)):
                    return True
    return False

def get_contained_bags(bag_dictionary, colour):
    num_bags = 0
    
    contained_bags = bag_dictionary.get(colour)

    if(contained_bags == None):
        return 0
    else:
        for spec in contained_bags:
            num_bags += (get_contained_bags(bag_dictionary, spec[0]) * spec[1]) + spec[1]

        return num_bags

lines = open("input.txt").readlines()

bag_dictionary = dict()

for line in lines:
    left, right = line.split(" contain ")
    left = left.replace(" bags", "")
    right = right.split(", ")
    right = [x.strip("\n").strip(".").replace(" bags", "").replace(" bag", "") for x in right]
    empty_bags = [x for x in right if x == "no other"]
    if len(empty_bags) > 0:
        continue
    right = [[x[2:], int(x[0])] for x in right]
    bag_dictionary[left] = right

bag_num = 0

for colour in bag_dictionary:
    if(contains_bag(bag_dictionary, colour, "shiny gold")):
        bag_num += 1

print("Part 1:", bag_num)

print("Part 2:", get_contained_bags(bag_dictionary, "shiny gold"))