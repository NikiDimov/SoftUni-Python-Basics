bad_scores = int(input())
counter_bad_scores = 0
counter_problems = 0
sum_scores = 0
problems = []
while True:
    problem = input()
    counter_problems += 1
    problems.append(problem)
    if problem == "Enough":
        counter_problems -= 1
        print(f"Average score: {sum_scores/counter_problems:.2f}")
        print(f"Number of problems: {counter_problems}")
        print(f"Last problem: {problems[-2]}")
        break
    score = int(input())
    sum_scores += score
    if score <= 4:
        counter_bad_scores += 1
        if counter_bad_scores == bad_scores:
            print(f"You need a break, {bad_scores} poor grades.")
            break


