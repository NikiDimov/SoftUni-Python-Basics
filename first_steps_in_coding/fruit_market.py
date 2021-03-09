strawberry_price = float(input())
bananas_kg = float(input())
oranges_kg = float(input())
raspberries_kg = float(input())
strawberries_kg = float(input())

raspberries_price = strawberry_price / 2
oranges_price = raspberries_price - (raspberries_price * 0.4)
bananas_price = raspberries_price - (raspberries_price * 0.8)
total_result = bananas_kg * bananas_price + oranges_kg * oranges_price + raspberries_kg * raspberries_price \
               + strawberries_kg * strawberry_price
print(total_result)
