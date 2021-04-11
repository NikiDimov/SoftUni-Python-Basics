movie = input()
counter_student = 0
counter_standard = 0
counter_kid = 0
while not movie == "Finish":
    seats = int(input())
    current_count = 0
    for _ in range(seats):
        command = input()
        if command == "student":
            counter_student += 1
        elif command == "standard":
            counter_standard += 1
        elif command == "kid":
            counter_kid += 1
        elif command == "End":
            break
        current_count += 1
    print(f"{movie} - {current_count / seats * 100:.2f}% full.")
    movie = input()
total_tickets = counter_kid + counter_student + counter_standard
print(f"Total tickets: {total_tickets}")
print(f"{counter_student / total_tickets * 100:.2f}% student tickets.")
print(f"{counter_standard / total_tickets * 100:.2f}% standard tickets.")
print(f"{counter_kid / total_tickets * 100:.2f}% kids tickets.")
