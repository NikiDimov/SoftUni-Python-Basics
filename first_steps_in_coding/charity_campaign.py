days = int(input())
cooks = int(input())
cakes = int(input())
gofretti = int(input())
pancakes = int(input())

result = days*cooks*(cakes*45 + gofretti*5.8 + pancakes*3.2)
result = result - result*1/8
print(result)


