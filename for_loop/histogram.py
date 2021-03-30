n = int(input())
my_list = [int(input()) for _ in range(n)]
p1 = []
p2 = []
p3 = []
p4 = []
p5 = []
for el in my_list:
    if el < 200:
        p1.append(el)
    elif el in range(200, 400):
        p2.append(el)
    elif el in range(400, 600):
        p3.append(el)
    elif el in range(600, 800):
        p4.append(el)
    else:
        p5.append(el)

print(f"{len(p1) / n * 100:.2f}%")
print(f"{len(p2) / n * 100:.2f}%")
print(f"{len(p3) / n * 100:.2f}%")
print(f"{len(p4) / n * 100:.2f}%")
print(f"{len(p5) / n * 100:.2f}%")
