player = input()
players = {}
while not player == "END":
    scores = int(input())
    players[player] = scores
    if scores >= 10:
        break
    player = input()

for key, value in players.items():
    if value == max(list(players.values())):
        print(f"{key} is the best player!")
        if value >= 3:
            print(f"He has scored {value} goals and made a hat-trick !!!")
        else:
            print(f"He has scored {value} goals.")
        break