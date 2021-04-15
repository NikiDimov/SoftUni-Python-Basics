price_for_luggage_over_20 = float(input())
weight_of_luggage = float(input())
days_till_taking_off = int(input())
total_luggage = int(input())

if weight_of_luggage < 10:
    tax = price_for_luggage_over_20 * 0.2
elif 10 <= weight_of_luggage <= 20:
    tax = price_for_luggage_over_20 * 0.5
else:
    tax = price_for_luggage_over_20

if days_till_taking_off > 30:
    tax = tax * 1.1
elif 7 <= days_till_taking_off <= 30:
    tax = tax * 1.15
else:
    tax = tax * 1.4

print(f"The total price of bags is: {tax * total_luggage:.2f} lv.")
