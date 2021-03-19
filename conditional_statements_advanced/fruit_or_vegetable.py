mapper = {
    "fruit": ["banana", "apple", "kiwi", "cherry", "lemon", "grapes"],
    "vegetable": ["tomato", "cucumber", "pepper", "carrot"]
}
product = input()


def fruit_or_veggie(p):
    for key, value in mapper.items():
        if p in value:
            return key
    return "unknown"


print(fruit_or_veggie(product))
