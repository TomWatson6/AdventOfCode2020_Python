

input = open("simple_input.txt").read()
parts = input.strip("mask = ").split("\nmask = ")

sections = []

for i in range(len(parts)):
    components = [x for x in parts[i].split("\nmem[")]
    mask = components[0]
    memory_alloc = components[1:]
    memory_alloc = [[int(x.split("] = ")[0]), 
        int(x.split("] = ")[1])] for x in memory_alloc]
    sections.append([mask, memory_alloc])
    
