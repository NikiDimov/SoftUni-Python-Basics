pages_to_read = int(input())
pages_per_hour = int(input())
days = int(input())


def hours_per_day(ptr, pph, d):
    return ptr / pph / d


print(hours_per_day(pages_to_read, pages_per_hour, days))
