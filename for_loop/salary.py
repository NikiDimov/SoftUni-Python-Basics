n = int(input())
salary = int(input())


def final_salary(n, salary):
    for _ in range(n):
        tab = input()
        if tab == "Facebook":
            salary -= 150
        elif tab == "Instagram":
            salary -= 100
        elif tab == "Reddit":
            salary -= 50
        if salary == 0:
            return "You have lost your salary."
    return salary


print(final_salary(n, salary))
