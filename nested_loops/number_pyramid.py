a = [i for i in range(1, int(input())+1)]
counter = 1
while a:
    print(*a[:counter])
    del a[:counter]
    counter += 1




