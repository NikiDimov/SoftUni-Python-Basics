n = int(input())
my_list = [int(input()) for _ in range(n)]
p1 = []
p2 = []
p3 = []

for el in my_list:
    if el%2 == 0:
        p1.append(el)
    if el%3 == 0:
        p2.append(el)
    if el%4 == 0:
        p3.append(el)

print(f"{len(p1) / n * 100:.2f}%")
print(f"{len(p2) / n * 100:.2f}%")
print(f"{len(p3) / n * 100:.2f}%")
