my_list = [float(input()) for _ in range(int(input()))]
odd_list = []
even_list = []
for i in range(len(my_list)):
    if i % 2 == 0:
        odd_list.append(my_list[i])
    else:
        even_list.append(my_list[i])

print(f"OddSum={sum(odd_list):.2f},")
if odd_list:
    print(f"OddMin={min(odd_list):.2f},")
    print(f"OddMax={max(odd_list):.2f},")
else:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
print(f"EvenSum={sum(even_list):.2f},")
if even_list:
    print(f"EvenMin={min(even_list):.2f},")
    print(f"EvenMax={max(even_list):.2f}")
else:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
