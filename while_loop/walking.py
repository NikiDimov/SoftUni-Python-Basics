target = 10000
next_steps = input()
get_target = False


def check_target(target):
    if target <= 0:
        return f"Goal reached! Good job!\n{abs(target)} steps over the goal!"
    return f"{abs(target)} more steps to reach goal."


while not next_steps == "Going home":
    next_steps = int(next_steps)
    target -= next_steps
    if target <= 0:
        print(check_target(target))
        get_target = True
        break
    next_steps = input()
if not get_target:
    next_steps = int(input())
    target -= next_steps
    print(check_target(target))
