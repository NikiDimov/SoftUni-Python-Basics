def converter(num, enter, exit):
    if enter == "m" and exit == "mm":
        return f"{num * 1000:.3f}"
    elif enter == "m" and exit == "cm":
        return f"{num * 100:.3f}"
    elif enter == "cm" and exit == "mm":
        return f"{num*10:.3f}"
    elif enter == "cm" and exit == "m":
        return f"{num/100:.3f}"
    elif enter == "mm" and exit == "m":
        return f"{num/1000:.3f}"
    elif enter == "mm" and exit =="cm":
        return f"{num/10:.3f}"


number = float(input())
enter = input()
exit = input()

print(converter(number, enter, exit))
