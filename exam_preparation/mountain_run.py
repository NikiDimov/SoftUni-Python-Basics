record = float(input())
distance = float(input())
time_for_meter = float(input())

slowing_down = distance // 50
georges_time = distance * time_for_meter + slowing_down * 30

if georges_time < record:
    print(f"Yes! The new record is {georges_time:.2f} seconds.")
else:
    print(f"No! He was {georges_time-record:.2f} seconds slower.")
