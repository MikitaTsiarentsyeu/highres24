def custom_sort(iterable, key_func):
    return sorted(iterable, key=key_func)

car = [("Toyota", 1937), ("Renault", 1899), ("Skoda", 1895), ("Hyundai", 1967), ("Kia", 1944), ("Volkswagen", 1937), ("BMW", 1916), ("Mercedes-Benz", 1926)]

print(custom_sort(car, lambda x: x[1]))