personal_money_per_day = float(input())
generated_money_per_day = float(input())
outcomes_for_all_days = float(input())
present_price = float(input())

total_money = personal_money_per_day*5 + generated_money_per_day*5 - outcomes_for_all_days

if total_money >= present_price:
    print(f"Profit: {total_money:.2f} BGN, the gift has been purchased.")
else:
    print(f"Insufficient money: {present_price - total_money:.2f} BGN.")


