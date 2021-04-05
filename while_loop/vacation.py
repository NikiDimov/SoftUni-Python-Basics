target_money = float(input())
current_money = float(input())
spend_money_counter = 0
days_counter = 0
while True:
    days_counter += 1
    text = input()
    money = float(input())
    if text == "spend":
        spend_money_counter += 1
        current_money -= money
        if current_money < 0:
            current_money = 0
        if spend_money_counter == 5:
            print("You can't save the money.")
            print(days_counter)
            break
    elif text == "save":
        spend_money_counter = 0
        current_money += money
        if current_money >= target_money:
            print(f"You saved the money for {days_counter} days.")
            break




