mapper = {
    "dog": "mammal",
    "crocodile": "reptile",
    "snake": "reptile",
    "tortoise": "reptile",

}
animal_type = input()


def animal(a):
    try:
        return mapper[a]
    except Exception:
        return "unknown"


print(animal(animal_type))
