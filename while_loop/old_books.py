def check_book():
    book = input()
    command = input()
    counter = 0
    while not command == "No More Books":
        if command == book:
            return f"You checked {counter} books and found it."
        counter += 1
        command = input()
    return f"The book you search is not here!\nYou checked {counter} books."


print(check_book())
