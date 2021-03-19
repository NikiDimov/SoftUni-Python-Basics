num = int(input())


def check_the_num(n):
    if n in range(-100, 101) and n != 0:
        return "Yes"
    return "No"


print(check_the_num(num))
