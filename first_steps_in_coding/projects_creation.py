def projects_creation(n, p):
    return f"The architect {n} will need {3 * p} hours to complete {p} project/s."


name = input()
projects = int(input())

print(projects_creation(name, projects))
