rent = int(input())


def budget(r):
    cake = r * 0.2
    spirits = cake - 0.45 * cake
    animator = 1 / 3 * r
    sums = r + cake + spirits + animator
    return sums


print(budget(rent))
