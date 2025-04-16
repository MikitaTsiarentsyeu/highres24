def custom_sort(iterable, key_func):
    return sorted(iterable, key=key_func)

people = [("Oleg", 45), ("Vanya", 24), ("Masha", 18), ("Gleb", 20), ("Laura", 27)]

print(custom_sort(people, lambda x: x[1]))