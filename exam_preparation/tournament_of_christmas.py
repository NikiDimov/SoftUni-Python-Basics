total_tournament_days = int(input())
total_money = 0
total_wins = 0
total_loses = 0
for day in range(total_tournament_days):
    current_day_money = 0
    count_wins = 0
    count_loses = 0
    command = input()
    while not command == "Finish":
        result = input()
        if result == "win":
            count_wins += 1
            current_day_money += 20
        elif result == "lose":
            count_loses += 1
        command = input()
    if count_wins > count_loses:
        current_day_money = current_day_money*1.1
        total_wins += 1
    else:
        total_loses += 1
    total_money += current_day_money
if total_wins > total_loses:
    print(f"You won the tournament! Total raised money: {total_money*1.2:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")
