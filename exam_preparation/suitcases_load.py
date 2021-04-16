trunk_capacity = float(input())
command = input()
counter = 0
full_trunk = False
while not command == "End":
    command = float(command)
    counter += 1
    if counter % 3 == 0:
        command = command * 1.1
    if trunk_capacity < command:
        full_trunk = True
        counter -= 1
        print("No more space!")
        break
    trunk_capacity -= command
    command = input()
if not full_trunk:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {counter} suitcases loaded.")
