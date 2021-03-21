mapper = {
    "Sofia": {range(0, 501): 0.05, range(501, 1001): 0.07, range(1001, 10001): 0.08},
    "Varna": {range(0, 501): 0.045, range(501, 1001): 0.075, range(1001, 10001): 0.1},
    "Plovdiv": {range(0, 501): 0.055, range(501, 1001): 0.08, range(1001, 10001): 0.12}
}
mapper_2 = {
    "Sofia": 0.12,
    "Varna": 0.13,
    "Plovdiv": 0.145
}
town = input()
s = float(input())


def commissions(town, s):
    if town in mapper and 0 <= s <= 10000:
        for key in mapper[town]:
            if int(s) in key:
                return f"{mapper[town][key] * s:.2f}"
    elif town in mapper_2 and s > 10000:
        return f"{mapper_2[town]*s:.2f}"
    return "error"


print(commissions(town, s))


