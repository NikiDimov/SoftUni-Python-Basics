mapper = {
    "working_days": {"banana": 2.50, "apple": 1.2, "orange": 0.85,
                     "grapefruit": 1.45, "kiwi": 2.7, "pineapple": 5.5, "grapes": 3.85},
    "weekends": {"banana": 2.7, "apple": 1.25, "orange": 0.9,
                 "grapefruit": 1.6, "kiwi": 3, "pineapple": 5.6, "grapes": 4.2}

}
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Saturday", "Sunday"]
fruit = input()
day = input()
quantity = float(input())


def fruit_shop(fruit, day, quantity):
    if day in days_of_week and fruit in mapper["working_days"]:
        return f"{mapper['working_days'][fruit] * quantity:.2f}"
    elif day in weekend and fruit in mapper["working_days"]:
        return f"{mapper['weekends'][fruit] * quantity:.2f}"
    return "error"


print(fruit_shop(fruit, day, quantity))
