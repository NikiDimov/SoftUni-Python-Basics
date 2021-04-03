n = input()
my_nums = []
while not n == "Stop":
    n = int(n)
    my_nums.append(n)
    n = input()
print(max(my_nums))
