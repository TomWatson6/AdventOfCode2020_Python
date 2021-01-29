

def play_game(players):
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

    return winner

def play_game_recursive(players):
    #print("play_game called...")

    record = dict()
    while len(players[0]) > 0 and len(players[1]) > 0:
        #print(players)
        hashable = tuple([tuple(x) for x in players])
        if record.get(hashable) == None:
            record[hashable] = True
        else:
            return (0, players[0]) # Player 1 wins
        
        player1 = players[0][0]
        player2 = players[1][0]
        players[0].remove(player1)
        players[1].remove(player2)

        sub_game_winner = -1

        if len(players[0]) > 0 and len(players[1]) > 0:
            if player1 <= len(players[0]) and player2 <= len(players[1]):
                new_players = []
                new_players.append(players[0][0:player1])
                new_players.append(players[1][0:player2])
                sub_game_winner = play_game_recursive(new_players)[0]

        if sub_game_winner == 0:
            players[0].append(player1)
            players[0].append(player2)
        elif sub_game_winner == 1:
            players[1].append(player2)
            players[1].append(player1)
        else:
            if player1 > player2:
                players[0].append(player1)
                players[0].append(player2)
            else:
                players[1].append(player2)
                players[1].append(player1)

    index = -1
    for x in range(len(players)):
        if len(players[x]) != 0:
            index = x
            break


    winner = [x for x in players if len(x) > 0]
    winner = (index, winner[0])

    return winner

f = open("input.txt")
lines = f.read()
f.close()

players = lines.split("\n\n")
players = [x.split("\n") for x in players]

for x in range(len(players)):
    players[x] = players[x][1:]
    players[x] = [p.strip() for p in players[x]]
    players[x] = [int(p) for p in players[x]]

players_copy = []

for x in players:
    player = []
    for y in x:
        player.append(y)
    players_copy.append(player)

winner = play_game(players)

total = 0

for x in range(len(winner)):
    total += winner[x] * (len(winner) - x)

print("Part 1:", total)

winner = play_game_recursive(players_copy)

total = 0

for x in range(len(winner[1])):
    total += winner[1][x] * (len(winner[1]) - x)

print("Part 2:", total)

players = players_copy

