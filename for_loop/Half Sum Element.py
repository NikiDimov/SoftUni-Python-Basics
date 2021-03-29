def my_list(n):
    return [int(input()) for _ in range(n)]


lists = my_list(int(input()))


def output(lists):
    for el in lists:
        if el == sum(lists)-el:
            return f"Yes\nSum = {el}"
    return f"No\nDiff = {abs(max(lists) - (sum(lists)-max(lists)))}"


print(output(lists))
