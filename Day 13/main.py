import math

input = open("input.txt").readlines()
depart = int(input[0].strip("\n"))
bus_times_strings = [x for x in input[1].split(",")]
bus_times = []

for bus_time in bus_times_strings:
    if bus_time == 'x':
        bus_times.append(bus_time)
    else:
        bus_times.append(int(bus_time))

lowest = 9999999
lowest_id = 0

for bus_time in bus_times:
    if bus_time != 'x':
        wait_time = bus_time - (depart % bus_time)
        if wait_time < lowest:
            lowest_id = bus_time
            lowest = wait_time

print("Part 1:", lowest_id * lowest)

def gcd(x, y):

   while y:
       x, y = y, x % y
   return x

def lcm(x, y):
   lcm = (x * y) // gcd(x,y)
   return lcm

ordered_bus_times = [x for x in bus_times if x != 'x']
ordered_bus_times.sort()

inc = ordered_bus_times[0]
index = 0

time = 0

while True:
    index += inc
    current = ordered_bus_times[0]

    inc_changed = False
    offset = bus_times.index(current)
    mult = (index + offset) / current

    if mult > int(mult):
        continue

    mult = int(mult)

    value = current * mult

    if value - index == offset:
        inc = lcm(current, inc)
        inc_changed = True
    
    if inc_changed:
        ordered_bus_times.remove(current)

    if len(ordered_bus_times) == 0:
        time = index
        break

print("Part 2:", time)