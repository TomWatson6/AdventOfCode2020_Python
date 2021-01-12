

class DoublyLinkedList:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return "Value: " + str(self.value) + " Left: " + str(self.left) + " Right: " + str(self.right)

    

def find(linked_list, value):
    return [x for x in linked_list if x.value == value][0]

f = open("simple_input.txt")
numbers = f.read()
f.close()

numbers = [int(char) for char in numbers]

linked_list = []

for x in range(len(numbers)):
    prev = numbers[(x - 1) % len(numbers)]
    after = numbers[(x + 1) % len(numbers)]
    linked_list.append(DoublyLinkedList(numbers[x], prev, after))

current = find(linked_list, numbers[0])
lowest = min([x.value for x in linked_list])
highest = max([x.value for x in linked_list])

for _ in range(10):
    temp_list = []
    #print(current)
    pointer = find(linked_list, current.right)
    for _ in range(3):
        temp_list.append(pointer)
        pointer = find(linked_list, pointer.right)
    
    find(linked_list, current.value).right = pointer.value
    pointer.left = find(linked_list, current.value).value
    destination_number = current.value
    destination = None
    while destination is None:
        if destination_number <= lowest:
            destination_number = highest
        else:
            destination_number -= 1
        if destination_number not in [x.value for x in temp_list]:
            destination = find(linked_list, destination_number)
    current = destination
    temp_list[0].left = destination.value
    temp_list[-1].right = find(linked_list, destination.right).value
    find(linked_list, destination.right).left = temp_list[-1].value
    destination.right = temp_list[0].value

    final = ""
    pos1 = linked_list.index([x for x in linked_list if x.value == 1][0])

    for x in range(len(linked_list)):
        position = (x + pos1) % len(linked_list)
        final += str(linked_list[position].value)

    print(final)

final = ""
pos1 = linked_list.index([x for x in linked_list if x.value == 1][0])

for x in range(len(linked_list)):
    position = (x + pos1) % len(linked_list)
    final += str(linked_list[position].value)

print("Part 1:", final)