n = int(input())


def odd_even_generator(n):
    odd_sum = 0
    even_sum = 0
    for i in range(1, n+1):
        current_num = int(input())
        if i % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
    if odd_sum == even_sum:
        return f"Yes\nSum = {odd_sum}"
    return f"No\nDiff = {abs(odd_sum - even_sum)}"


print(odd_even_generator(n))
