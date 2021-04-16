total_days = int(input())
total_amount_food = float(input())
eaten_food_by_cat = 0
eaten_food_by_dog = 0
total_eaten_food = 0
total_eaten_biscuits = 0

for day in range(1, total_days+1):
    dog_eat = int(input())
    cat_eat = int(input())
    eaten_food_by_cat += cat_eat
    eaten_food_by_dog += dog_eat
    total_eaten_food += dog_eat + cat_eat
    if day % 3 == 0:
        total_eaten_biscuits += (dog_eat + cat_eat) * 0.1
print(f"Total eaten biscuits: {round(total_eaten_biscuits)}gr.\n"
      f"{total_eaten_food / total_amount_food * 100:.2f}% of the food has been eaten.\n"
      f"{eaten_food_by_dog / total_eaten_food * 100:.2f}% eaten from the dog.\n"
      f"{eaten_food_by_cat / total_eaten_food * 100:.2f}% eaten from the cat.")
