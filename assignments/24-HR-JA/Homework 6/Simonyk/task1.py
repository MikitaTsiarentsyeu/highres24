def names(iterable, key_func):
    return sorted(iterable, key=key_func)

name = [("Yurii", 2006), ("Vitalii", 1999), ("Nastya", 2000), ("Max", 1987), ("Katya", 1978), ("Valerii", 1937), ("Vasya", 2010), ("Igor", 2001)]

print(names (name, lambda x: x[1]))