days = int(input())
room = input()
assessment = input()


def negative_ot_positive(assessment, total_price):
    if assessment == "negative":
        print(f"{total_price - total_price * 0.1:.2f}")
    else:
        print(f"{total_price * 1.25:.2f}")


def room_for_one_person(days, assessment):
    total_price = (days - 1) * 18
    negative_ot_positive(assessment, total_price)


def apartment(days, assessment):
    total_price = (days - 1) * 25
    if days <= 10:
        total_price -= total_price * 0.3
    elif 10 < days <= 15:
        total_price -= total_price * 0.35
    else:
        total_price -= total_price * 0.5
    negative_ot_positive(assessment, total_price)


def president_apartment(days, assessment):
    total_price = (days - 1) * 35
    if days <= 10:
        total_price -= total_price * 0.1
    elif 10 < days <= 15:
        total_price -= total_price * 0.15
    else:
        total_price -= total_price * 0.2
    negative_ot_positive(assessment, total_price)


if room == "room for one person":
    room_for_one_person(days, assessment)
elif room == "apartment":
    apartment(days, assessment)
elif room == "president apartment":
    president_apartment(days, assessment)

