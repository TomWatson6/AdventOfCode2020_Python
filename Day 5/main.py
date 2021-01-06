lines = open("input.txt").readlines()
seats = []

for line in lines:
    row_str = line[:7]
    col_str = line[7:]
    row_bin_str = row_str.replace("F", "0").replace("B", "1").strip("\n")
    col_bin_str = col_str.replace("L", "0").replace("R", "1").strip("\n")
    row = int(row_bin_str, 2)
    col = int(col_bin_str, 2)
    seats.append([row, col, row * 8 + col])

output = max([x[2] for x in seats])

print("Part 1:", output)

seats_ids = [x[2] for x in seats]
seats_ids.sort()

for x in range(1, len(seats_ids)):
    if seats_ids[x] - seats_ids[x - 1] > 1:
        print("Part 2:", seats_ids[x] - 1)
        break