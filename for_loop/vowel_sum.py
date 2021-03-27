mapper = {"a": 1, "e": 2, "i": 3, "o": 4, "u": 5}


def text(string):
    return sum(mapper[el] for el in string if el in mapper)


print(text(input()))
