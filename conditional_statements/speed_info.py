speed = float(input())


def speed_info(s):
    if s <= 10:
        return "slow"
    elif 10 < s <= 50:
        return "average"
    elif 50 < s <= 150:
        return "fast"
    elif 150 < s <= 1000:
        return "ultra fast"
    else:
        return "extremely fast"


print(speed_info(speed))
