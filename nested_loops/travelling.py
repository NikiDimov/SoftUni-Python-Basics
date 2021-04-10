destination = input()
while not destination == "End":
    budget = float(input())
    while not budget <= 0:
        current_money = float(input())
        budget -= current_money
    print(f"Going to {destination}!")
    destination = input()

