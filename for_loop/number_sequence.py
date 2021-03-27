num = int(input())


def my_sequence(num):
    sequence = [int(input()) for _ in range(num)]
    return sequence


numbers = my_sequence(num)


def output(nums):
    return f"Max number: {max(nums)}\nMin number: {min(nums)}"


print(output(numbers))
