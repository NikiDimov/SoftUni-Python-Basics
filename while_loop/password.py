name = input()
password = input()
validate_password = input()
while not validate_password == password:
    validate_password = input()
print(f"Welcome {name}!")
