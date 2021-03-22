budget = float(input())
season = input()


def destination(budget):
    if budget <= 100:
        return "Bulgaria"
    elif budget <= 1000:
        return "Balkans"
    return "Europe"


def type_journey(season):
    place = destination(budget)
    if season == "summer":
        if place == "Bulgaria" or place == "Balkans":
            return "Camp"
    return "Hotel"


def output(spent_money):
    print(f"Somewhere in {destination(budget)}")
    print(f"{type_journey(season)} - {spent_money:.2f}")


def journey(budget, season):
    if budget <= 100:
        if season == "summer":
            spent_money = budget * 0.3
            output(spent_money)
        elif season == "winter":
            spent_money = budget * 0.7
            output(spent_money)
    elif budget <= 1000:
        if season == "summer":
            spent_money = budget * 0.4
            output(spent_money)
        elif season == "winter":
            spent_money = budget * 0.8
            output(spent_money)
    else:
        spent_money = budget * 0.9
        output(spent_money)


journey(budget, season)
