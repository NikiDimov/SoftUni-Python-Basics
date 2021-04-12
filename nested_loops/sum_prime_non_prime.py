command = input()
sum_prime = 0
sum_non_prime = 0
while not command == "stop":
    command = int(command)
    is_prime = True
    if command < 0:
        print("Number is negative.")
        command = input()
        continue
    for i in range(2, command):
        if command % i == 0:
            sum_non_prime += command
            is_prime = False
            break
    if is_prime:
        sum_prime += command

    command = input()
print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_non_prime}")