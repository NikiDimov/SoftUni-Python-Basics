budget = float(input())
extras = int(input())
price_clothes = float(input())

decor = budget * 0.1


def movie_maker(budget, extras, price_clothes):
    if extras > 150:
        price_clothes -= price_clothes * 0.1
    total = price_clothes * extras + decor
    if total > budget:
        return f"Not enough money!\nWingard needs {total - budget:.2f} leva more."
    return f"Action!\nWingard starts filming with {budget - total:.2f} leva left."


print(movie_maker(budget, extras, price_clothes))
