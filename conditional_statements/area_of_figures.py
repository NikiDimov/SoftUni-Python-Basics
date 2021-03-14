from math import pi


def area(figure):
    if figure == "square":
        return float(input()) ** 2
    elif figure == "rectangle":
        return float(input()) * float(input())
    elif figure == "circle":
        return pow(float(input()), 2) * pi
    elif figure == "triangle":
        return float(input()) * float(input()) / 2


print(f"{area(input()):.3f}")
