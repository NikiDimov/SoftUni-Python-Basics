age = float(input())
gender = input()


def title(age, gender):
    if age >= 16:
        if gender == "m":
            return "Mr."
        return "Ms."
    else:
        if gender == "m":
            return "Master"
        return "Miss"


print(title(age, gender))
