fruit = input()
set_size = input()
total_sets = int(input())
total_money = 0
small_mapper = {"Watermelon": 56 * 2, "Mango": 36.66 * 2, "Pineapple": 42.1 * 2, "Raspberry": 20 * 2}
big_mapper = {"Watermelon": 28.7 * 5, "Mango": 19.6 * 5, "Pineapple": 24.8 * 5, "Raspberry": 15.2 * 5}

if set_size == "small":
    total_money += small_mapper[fruit] * total_sets
elif set_size == "big":
    total_money += big_mapper[fruit] * total_sets

if 400 <= total_money <= 1000:
    total_money -= total_money * 0.15
elif total_money > 1000:
    total_money -= total_money * 0.5

print(f"{total_money:.2f} lv.")
