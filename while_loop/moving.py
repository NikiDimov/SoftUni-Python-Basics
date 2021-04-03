width = int(input())
length = int(input())
height = int(input())
cubic_meters = width * length * height
command = input()
while not command == "Done":
    command = int(command)
    cubic_meters -= command
    if cubic_meters < 0:
        print(f"No more free space! You need {abs(cubic_meters)} Cubic meters more.")
        exit(0)
    command = input()
print(f"{cubic_meters} Cubic meters left.")
