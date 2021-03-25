start_exam_hours = int(input())
start_exam_minutes = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())

total_minutes_exam = start_exam_hours * 60 + start_exam_minutes
total_minutes_arrival = arrival_hours * 60 + arrival_minutes


def on_time_or_not(total_minutes_exam, total_minutes_arrival):
    difference = abs(total_minutes_exam - total_minutes_arrival)
    if total_minutes_exam > total_minutes_arrival:
        if difference <= 30:
            return f"On time\n{difference} minutes before the start"
        elif 30 < difference <= 59:
            return f"Early\n{difference} minutes before the start"
        return f"Early\n{difference // 60}:{difference % 60:02d} hours before the start"
    elif total_minutes_arrival > total_minutes_exam:
        if difference <= 59:
            return f"Late\n{difference} minutes after the start"
        return f"Late\n{difference // 60}:{difference % 60:02d} hours after the start"
    return "On time"


print(on_time_or_not(total_minutes_exam, total_minutes_arrival))



