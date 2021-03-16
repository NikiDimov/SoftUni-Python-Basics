incomes = float(input())
average_grade = float(input())
minimal_salary = float(input())

if 4.5 <= average_grade < 5.5 and incomes < minimal_salary:
    scholarship = minimal_salary * 0.35
    print(f"You get a Social scholarship {int(scholarship)} BGN")
elif average_grade >= 5.5 and incomes >= minimal_salary:
    scholarship = average_grade * 25
    print(f"You get a scholarship for excellent results {int(scholarship)} BGN")
elif average_grade >= 5.5 and incomes < minimal_salary:
    scholarship_social = minimal_salary * 0.35
    scholarship_excellent = average_grade * 25
    if scholarship_social > scholarship_excellent:
        print(f"You get a Social scholarship {int(scholarship_social)} BGN")
    else:
        print(f"You get a scholarship for excellent results {int(scholarship_excellent)} BGN")
else:
    print(f"You cannot get a scholarship!")
