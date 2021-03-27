n = int(input())


def backwards(n):
    return '\n'.join(map(str, (i for i in range(n, 0, -1))))


print(backwards(n))
