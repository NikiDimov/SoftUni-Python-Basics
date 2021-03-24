month = input()
nights = int(input())


def discount(month, nights, type_of_room):
    if type_of_room == "Apartment" and nights > 14:
        return 0.1
    elif type_of_room == "Studio":
        if month == "May" or month == "October":
            if 7 < nights <= 14:
                return 0.05
            elif nights > 14:
                return 0.3
        elif (month == "June" or month == "September") and nights > 14:
            return 0.2
    return 0


def output(current_price, type_of_room):
    print(f"{type_of_room}: {current_price:.2f} lv.")


def hotel_room(type_of_room, month, nights):
    discounts = discount(month, nights, type_of_room)
    current_price = 0
    if type_of_room == "Studio":
        if month == "May" or month == "October":
            current_price += 50 * nights
        elif month == "June" or month == "September":
            current_price += 75.2 * nights
        else:
            current_price += 76 * nights
        current_price -= current_price*discounts
        return output(current_price, type_of_room)
    elif type_of_room == "Apartment":
        if month == "May" or month == "October":
            current_price += 65 * nights
        elif month == "June" or month == "September":
            current_price += 68.70 * nights
        else:
            current_price += 77 * nights
        current_price -= current_price * discounts
        return output(current_price, type_of_room)


hotel_room("Apartment", month, nights)
hotel_room("Studio", month, nights)
