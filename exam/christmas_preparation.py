PAPER_PRICE = 5.8
FABRIC_PRICE = 7.2
GLUE_PRICE_LITTER = 1.2

total_paper = int(input())
total_fabric = int(input())
total_glue = float(input())
percentage_discount = float(input())

money_needed = total_paper * PAPER_PRICE + total_fabric * FABRIC_PRICE + total_glue * GLUE_PRICE_LITTER

print(f"{money_needed - money_needed * percentage_discount / 100:.3f}")

