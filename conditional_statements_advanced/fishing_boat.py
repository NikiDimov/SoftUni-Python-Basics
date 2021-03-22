budget = int(input())
season = input()
fishmen = int(input())


def discounts(fishmen):
    if fishmen <= 6:
        return 0.1
    elif 7 < fishmen <= 11:
        return 0.15
    return 0.25


def output(budget, outcomes):
    if budget >= outcomes:
        print(f"Yes! You have {budget - outcomes:.2f} leva left.")
    else:
        print(f"Not enough money! You need {outcomes - budget:.2f} leva.")


def fishing(budget, season, fishmen):
    outcomes = 0
    if season == "Spring":
        outcomes += 3000
        outcomes -= outcomes * discounts(fishmen)
        if fishmen % 2 == 0:
            outcomes -= outcomes * 0.05
        output(budget, outcomes)
    elif season == "Summer":
        outcomes += 4200
        outcomes -= outcomes * discounts(fishmen)
        if fishmen % 2 == 0:
            outcomes -= outcomes * 0.05
        output(budget, outcomes)
    elif season == "Autumn":
        outcomes += 4200
        outcomes -= outcomes * discounts(fishmen)
        output(budget, outcomes)
    else:
        outcomes += 2600
        outcomes -= outcomes * discounts(fishmen)
        if fishmen % 2 == 0:
            outcomes -= outcomes * 0.05
        output(budget, outcomes)


fishing(budget, season, fishmen)
