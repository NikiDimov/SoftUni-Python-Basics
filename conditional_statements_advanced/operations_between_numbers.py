N1 = int(input())
N2 = int(input())
operator = input()


def calculator(operator, N1, N2):
    try:
        result = eval(f"{N1}{operator}{N2}")
    except:
        return ZeroDivisionError(f"Cannot divide {N1} by zero")
    if operator == "+" or operator == "-" or operator == "*":
        return f"{N1} {operator} {N2} = {result} - {'even' if result % 2 == 0 else 'odd'}"
    elif operator == "/":
        return f"{N1} / {N2} = {result:.2f}"
    return f"{N1} % {N2} = {result}"


print(calculator(operator, N1, N2))
