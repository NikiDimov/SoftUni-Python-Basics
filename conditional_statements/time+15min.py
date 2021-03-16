from datetime import datetime, timedelta

hours = int(input())
minutes = input()
minutes = int(minutes)
time_object = datetime(1, 1, 1, hour=hours, minute=minutes)
time_object += timedelta(minutes=15)
print(f"{time_object.hour}:{time_object.minute:02d}")
