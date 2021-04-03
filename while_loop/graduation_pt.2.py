name = input()
grade = 1
retake = 1
sums = 0
while not grade > 12:
    assessment = float(input())
    if assessment >= 4:
        grade += 1
        sums += assessment
    else:
        if not retake == 0:
            retake -= 1
        else:
            print(f"{name} has been excluded at {grade} grade")
            exit(0)
print(f"{name} graduated. Average grade: {sums/12:.2f}")

