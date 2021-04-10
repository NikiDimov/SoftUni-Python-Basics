start = int(input())
end = int(input())
magic = int(input())


def sum_of_two(start, end, magic):
    counter = 0
    for x in range(start, end + 1):
        for y in range(start, end + 1):
            counter += 1
            if x + y == magic:
                return f"Combination N:{counter} ({x} + {y} = {magic})"
    return f"{counter} combinations - neither equals {magic}"


print(sum_of_two(start, end, magic))
