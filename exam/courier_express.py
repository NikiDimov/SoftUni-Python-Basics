weight_package = float(input())
type_delivery = input()
distance = int(input())
price = 0

if type_delivery == "standard":
    if weight_package < 1:
        price = 3 * distance
    elif 1 <= weight_package < 10:
        price = 5 * distance
    elif 10 <= weight_package < 40:
        price = 10 * distance
    elif 40 <= weight_package < 90:
        price = 15 * distance
    elif 90 <= weight_package < 150:
        price = 20 * distance
elif type_delivery == "express":
    if weight_package < 1:
        price = distance * 3 + (weight_package * 0.80 * 3 * distance)
    elif 1 <= weight_package < 10:
        price = 5 * distance + (weight_package * 0.40 * 5 * distance)
    elif 10 <= weight_package < 40:
        price = 10 * distance + (weight_package * 0.05 * 10 * distance)
    elif 40 <= weight_package < 90:
        price = 15 * distance + (weight_package * 0.02 * 15 * distance)
    elif 90 <= weight_package < 150:
        price = 20 * distance + (weight_package * 0.01 * 20 * distance)

print(f"The delivery of your shipment with weight of {weight_package:.3f} kg. would cost {price / 100:.2f} lv.")
