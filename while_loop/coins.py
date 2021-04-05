coins = float(input())
coins = int(coins * 100)
counter = 0

lists = [200, 100, 50, 20, 10, 5, 2, 1]

while coins > 0:
    for el in lists:
        if el <= coins:
            coins -= el
            counter += 1
            break

print(counter)
