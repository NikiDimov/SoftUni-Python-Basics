total_balls = int(input())
points = 0
counter_red = 0
counter_orange = 0
counter_yellow = 0
counter_white = 0
counter_black = 0
counter_other = 0

for _ in range(total_balls):
    command = input()
    if command == "red":
        points += 5
        counter_red += 1
    elif command == "orange":
        points += 10
        counter_orange += 1
    elif command == "yellow":
        points += 15
        counter_yellow += 1
    elif command == "white":
        points += 20
        counter_white += 1
    elif command == "black":
        points = points // 2
        counter_black += 1
    else:
        counter_other += 1

print(f"Total points: {points}\n"
      f"Points from red balls: {counter_red}\n"
      f"Points from orange balls: {counter_orange}\n"
      f"Points from yellow balls: {counter_yellow}\n"
      f"Points from white balls: {counter_white}\n"
      f"Other colors picked: {counter_other}\n"
      f"Divides from black balls: {counter_black}")
