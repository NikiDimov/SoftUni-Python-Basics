first_num = input()
second_num = input()

for x1 in range(int(first_num[0]), int(second_num[0]) + 1):
    if x1 != 0 and x1 % 2 != 0:
        for x2 in range(int(first_num[1]), int(second_num[1]) + 1):
            if x2 != 0 and x2 % 2 != 0:
                for x3 in range(int(first_num[2]), int(second_num[2]) + 1):
                    if x3 != 0 and x3 % 2 != 0:
                        for x4 in range(int(first_num[3]), int(second_num[3]) + 1):
                            if x4 != 0 and x4 % 2 != 0:
                                print(f"{x1}{x2}{x3}{x4}", end=' ')