def numbers(n):
    return '\n'.join(map(str, [i for i in range(1, n+1, 3)]))


number = int(input())
print(numbers(number))
