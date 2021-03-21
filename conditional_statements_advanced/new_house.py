flowers = {"Roses": 5, "Dahlias": 3.8, "Tulips": 2.8, "Narcissus": 3, "Gladiolus": 2.5}
flower = input()
pieces = int(input())
budget = int(input())


def output(final_price, budget):
    if final_price <= budget:
        print(f"Hey, you have a great garden with {pieces} {flower} and {budget - final_price:.2f} leva left.")
    else:
        print(f"Not enough money, you need {final_price - budget:.2f} leva more.")


def bouquet(flower, pieces, budget):
    if flower == "Roses":
        final_price = flowers[flower] * pieces
        if pieces > 80:
            final_price -= final_price * 0.1
        output(final_price, budget)
    elif flower == "Dahlias":
        final_price = flowers[flower] * pieces
        if pieces > 90:
            final_price -= final_price * 0.15
        output(final_price, budget)
    elif flower == "Tulips":
        final_price = flowers[flower] * pieces
        if pieces > 80:
            final_price -= final_price * 0.15
        output(final_price, budget)
    elif flower == "Narcissus":
        final_price = flowers[flower] * pieces
        if pieces < 120:
            final_price *= 1.15
        output(final_price, budget)
    elif flower == "Gladiolus":
        final_price = flowers[flower] * pieces
        if pieces < 80:
            final_price *= 1.2
        output(final_price, budget)


bouquet(flower, pieces, budget)
