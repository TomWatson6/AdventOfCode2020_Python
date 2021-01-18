

f = open("input.txt")
lines = f.read()
f.close()

players = lines.split("\n\n")
players = [x.split("\n") for x in players]

for x in range(len(players)):
    players[x] = players[x][1:]
    players[x] = [p.strip() for p in players[x]]
    players[x] = [int(p) for p in players[x]]


while len(players[0]) > 0 and len(players[1]) > 0:
    player1 = players[0][0]
    player2 = players[1][0]
    players[0].remove(player1)
    players[1].remove(player2)
    if player1 > player2:
        players[0].append(player1)
        players[0].append(player2)
    else:
        players[1].append(player2)
        players[1].append(player1)

winner = [x for x in players if len(x) > 0]
winner = winner[0]

total = 0

for x in range(len(winner)):
    total += winner[x] * (len(winner) - x)

print("Part 1:", total)