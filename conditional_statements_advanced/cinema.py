type_projection = input()
rows = int(input())
cols = int(input())


def cinema_incomes(type, r, c):
    if type == "Premiere":
        return f"{r * c * 12:.2f} leva"
    elif type == "Normal":
        return f"{r * c * 7.5:.2f} leva"
    elif type == "Discount":
        return f"{r * c * 5:.2f} leva"


print(cinema_incomes(type_projection, rows, cols))
