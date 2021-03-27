age = int(input())
washing_machine_price = float(input())
toy_price = int(input())


def safe_money(age, toy_price):
    money = 0
    counter = 0
    for birthday in range(1, age + 1):
        if birthday % 2 == 0:
            counter += 1
            money += 10*counter-1
        else:
            money += toy_price
    return money


money = safe_money(age, toy_price)


def output(money, washing_machine_price):
    if money >= washing_machine_price:
        return f"Yes! {money - washing_machine_price:.2f}"
    return f"No! {washing_machine_price - money:.2f}"


print(output(money, washing_machine_price))
