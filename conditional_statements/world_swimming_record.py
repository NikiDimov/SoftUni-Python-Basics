record = float(input())
distance = float(input())
time_per_meter = float(input())

time_all_distance = distance*time_per_meter + (distance//15)*12.5

if time_all_distance<record:
    print(f"Yes, he succeeded! The new world record is {time_all_distance:.2f} seconds.")
else:
    print(f"No, he failed! He was {time_all_distance-record:.2f} seconds slower.")
