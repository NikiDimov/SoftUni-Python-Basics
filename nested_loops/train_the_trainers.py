n = int(input())
command = input()
counter = 0
total_result = 0
while not command == "Finish":
    current_result = 0
    for _ in range(n):
        rate = float(input())
        current_result += rate
        total_result += rate
        counter += 1
    print(f"{command} - {current_result / n:.2f}.")
    command = input()
print(f"Student's final assessment is {total_result / counter:.2f}.")