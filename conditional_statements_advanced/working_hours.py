hour = int(input())
day = input()
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


def working_hour(day, hour):
    if day in days_of_week and hour in range(10, 19):
        return "open"
    return "closed"


print(working_hour(day, hour))
