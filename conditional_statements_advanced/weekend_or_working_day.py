mapper = {"Monday": "Working day",
          "Tuesday": "Working day",
          "Wednesday": "Working day",
          "Thursday": "Working day",
          "Friday": "Working day",
          "Saturday": "Weekend",
          "Sunday": "Weekend"
          }
day = input()


def try_day(d):
    try:
        return mapper[d]
    except Exception:
        return "Error"


print(try_day(day))
