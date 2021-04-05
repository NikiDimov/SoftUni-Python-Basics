length = int(input())
width = int(input())
area = length * width
cake_is_over = False
command = input()
while not command == "STOP":
    command = int(command)
    area -= command
    if area < 0:
        print(f"No more cake left! You need {abs(area)} pieces more.")
        cake_is_over = True
        break
    command = input()
if not cake_is_over:
    print(f"{area} pieces are left.")

