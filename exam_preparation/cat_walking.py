minutes_in_walking = int(input())
total_walking_per_day = int(input())
taken_calories_per_day = int(input())

total_burned_calories = minutes_in_walking * total_walking_per_day * 5

if total_burned_calories >= taken_calories_per_day*0.5:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {total_burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {total_burned_calories}.")