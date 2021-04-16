money = float(input())
gender = input()
age = int(input())
sport = input()
sum_needed = 0
male_mapper = {"Gym": 42, "Boxing": 41, "Yoga": 45, "Zumba": 34, "Dances": 51, "Pilates": 39}
female_mapper = {"Gym": 35, "Boxing": 37, "Yoga": 42, "Zumba": 31, "Dances": 53, "Pilates": 37}
if gender == "m":
    sum_needed += male_mapper[sport]
elif gender == "f":
    sum_needed += female_mapper[sport]
if age <= 19:
    sum_needed -= sum_needed * 0.2
if money >= sum_needed:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${sum_needed - money:.2f} more.")
