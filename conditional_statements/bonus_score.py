num = int(input())


def bonus_score(n):
    bonus = 0
    if n % 2 == 0:
        bonus += 1
    if n % 5 == 0 and n % 10 != 0:
        bonus += 2

    if n <= 100:
        bonus += 5
    elif 100 < n < 1000:
        bonus += n * 0.2
    else:
        bonus += n * 0.1

    return bonus


print(bonus_score(num))
print(bonus_score(num) + num)
