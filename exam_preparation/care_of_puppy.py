total_food = int(input())
total_food = total_food * 1000
command = input()
while not command == "Adopted":
    command = int(command)
    total_food -= command
    command = input()
if total_food >= 0:
    print(f"Food is enough! Leftovers: {total_food} grams.")
else:
    print(f"Food is not enough. You need {abs(total_food)} grams more.")

