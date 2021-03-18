mapper = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
num = int(input())


def day_of_week(n):
    try:
        return mapper[n]
    except Exception:
        return "Error"


print(day_of_week(num))
