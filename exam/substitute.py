k = int(input())
l = int(input())
m = int(input())
n = int(input())
counter = 0
for x1 in range(k, 9):
    if x1 % 2 == 0:
        for x2 in range(9, l - 1, -1):
            if x2 % 2 != 0:
                for x3 in range(m, 9):
                    if x3 % 2 == 0:
                        for x4 in range(9, n - 1, -1):
                            if x4 % 2 != 0:
                                if f"{x1}{x2}" == f"{x3}{x4}":
                                    print("Cannot change the same player.")
                                else:
                                    print(f"{x1}{x2} - {x3}{x4}")
                                    counter += 1
                                    if counter == 6:
                                        exit(0)
