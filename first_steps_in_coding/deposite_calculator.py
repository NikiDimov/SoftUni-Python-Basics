deposit = float(input())
term = int(input())
year_percent = float(input())


def calculator(d, t, y):
    return d + t * ((d * y/100) / 12)


print(calculator(deposit, term, year_percent))
