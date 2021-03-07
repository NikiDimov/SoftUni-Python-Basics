def yard_greening(y):
    price_per_sqm = 7.61
    first_price = y * price_per_sqm
    discount = first_price * 0.18
    final_price = first_price - discount
    return f"The final price is: {final_price} lv.\nThe discount is: {discount} lv."


yards = float(input())
print(yard_greening(yards))
