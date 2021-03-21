degrees = int(input())
time = input()
outfit = ["Sweatshirt", "Shirt", "T-Shirt", "Swim Suit"]
shoes = ["Sneakers", "Moccasins", "Sandals", "Barefoot"]


def get_your_outfit(degrees, time):
    if time == "Morning":
        if 10 <= degrees <= 18:
            return f"It's {degrees} degrees, get your {outfit[0]} and {shoes[0]}."
        elif 18 < degrees <= 24:
            return f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}."
        elif degrees >= 25:
            return f"It's {degrees} degrees, get your {outfit[2]} and {shoes[2]}."
    elif time == "Afternoon":
        if 10 <= degrees <= 18:
            return f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}."
        elif 18 < degrees <= 24:
            return f"It's {degrees} degrees, get your {outfit[2]} and {shoes[2]}."
        elif degrees >= 25:
            return f"It's {degrees} degrees, get your {outfit[3]} and {shoes[3]}."
    return f"It's {degrees} degrees, get your {outfit[1]} and {shoes[1]}."


print(get_your_outfit(degrees, time))


