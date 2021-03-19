mapper = {
    "Monday": 12,
    "Tuesday": 12,
    "Wednesday": 14,
    "Thursday": 14,
    "Friday": 12,
    "Saturday": 16,
    "Sunday": 16

}
day_of_week = input()


def cinema_ticket(day):
    return mapper[day]


print(cinema_ticket(day_of_week))
