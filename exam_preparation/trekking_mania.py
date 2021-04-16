total_groups = int(input())
cliffhangers = 0
musala_counter = 0
monblan_counter = 0
kilim_counter = 0
k2_counter = 0
everest_counter = 0

for group in range(1, total_groups + 1):
    total_players = int(input())
    cliffhangers += total_players
    if total_players <= 5:
        musala_counter += total_players
    elif 6 <= total_players <= 12:
        monblan_counter += total_players
    elif 13 <= total_players <= 25:
        kilim_counter += total_players
    elif 26 <= total_players <= 40:
        k2_counter += total_players
    elif total_players >= 41:
        everest_counter += total_players
print(f"{musala_counter/cliffhangers*100:.2f}%\n{monblan_counter/cliffhangers*100:.2f}%\n"
      f"{kilim_counter/cliffhangers*100:.2f}%\n{k2_counter/cliffhangers*100:.2f}%\n"
      f"{everest_counter/cliffhangers*100:.2f}%")

