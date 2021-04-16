PENS_PRICE = 5.8
MARKERS_PRICE = 7.2
DETERGENT_PRICE_LITTER = 1.2

total_pens = int(input())
total_markers = int(input())
litters_of_detergent = float(input())
discount_percentage = float(input())

result = total_pens*PENS_PRICE + total_markers*MARKERS_PRICE + litters_of_detergent*DETERGENT_PRICE_LITTER
print(f"{result - result*discount_percentage/100:.3f}")
