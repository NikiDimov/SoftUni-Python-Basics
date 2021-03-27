n = int(input())


def enter_nums(n):
    return sum(int(input()) for _ in range(n))


def left_nums():
    return enter_nums(n)


def right_nums():
    return enter_nums(n)


def output(left, right):
    if left == right:
        return f"Yes, sum = {left}"
    return f"No, diff = {abs(left - right)}"


left = left_nums()
right = right_nums()

print(output(left, right))
