from math import pi, floor


def rad_to_deg(rad):
    deg = rad * 180 / pi
    return floor(deg)


radian = float(input())

print(rad_to_deg(radian))
