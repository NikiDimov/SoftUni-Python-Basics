command = input()
total_days = 5
counter = 1
start_point = 5364
is_reached = False
while not command == "END":
    if command == "Yes":
        total_days -= 1
        counter += 1
    if total_days == 0:
        break
    next_meters = int(input())
    start_point += next_meters
    if start_point >= 8848:
        is_reached = True
        break

    command = input()
if is_reached:
    print(f"Goal reached for {counter} days!")
else:
    print(f"Failed!\n{start_point}")
