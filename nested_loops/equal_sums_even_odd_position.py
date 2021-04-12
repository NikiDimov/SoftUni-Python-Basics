start = int(input())
end = int(input())
for current_digit in range(start, end + 1):
    sum_even = 0
    sum_odd = 0
    current_digit = str(current_digit)
    for index in range(6):
        if index % 2 == 0:
            sum_odd += int(current_digit[index])
        else:
            sum_even += int(current_digit[index])
    if sum_even == sum_odd:
        print(current_digit, end=' ')
