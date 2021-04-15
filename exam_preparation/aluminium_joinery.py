total_joinery = int(input())
type_joinery = input()
type_delivery = input()
total_price = 0

if type_joinery == "90X130":
    price = 110
    if 30 <= total_joinery <= 60:
        price = price - price * 0.05
    elif total_joinery > 60:
        price = price - price * 0.08
elif type_joinery == "100X150":
    price = 140
    if 40 <= total_joinery <= 80:
        price = price - price * 0.06
    elif total_joinery > 80:
        price = price - price * 0.1
elif type_joinery == "130X180":
    price = 190
    if 20 <= total_joinery <= 50:
        price = price - price * 0.07
    elif total_joinery > 50:
        price = price - price * 0.12
elif type_joinery == "200X300":
    price = 250
    if 25 <= total_joinery <= 50:
        price = price - price * 0.09
    elif total_joinery > 50:
        price = price - price * 0.14

if type_delivery == "With delivery":
    total_price = price * total_joinery + 60
else:
    total_price = price * total_joinery
if total_joinery >= 99:
    total_price = total_price - total_price * 0.04
if total_joinery < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
