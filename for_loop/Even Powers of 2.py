n = int(input())


def even_powers(n):
    return '\n'.join(map(str, [pow(2, i) for i in range(n+1) if i % 2 == 0]))


print(even_powers(n))
