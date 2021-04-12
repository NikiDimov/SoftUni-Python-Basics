n = int(input())


def check_for_special(special):
    for el in special:
        try:
            if n % int(el) == 0:
                continue
            return
        except ZeroDivisionError:
            return
    return special


for special in range(1111, 10000):
    special = str(special)
    if check_for_special(special):
        print(check_for_special(special), end=' ')
