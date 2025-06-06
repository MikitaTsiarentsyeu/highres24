import math
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def Input(arg):
    while True:
        d = input(f"введите значения елемента {arg}: ")
        if is_number(d):
            return float(d)
        else:
            print("ввести можно только число")

a = Input("a")
b = Input("b")
c = Input("c")
print(f"{a}, {b}, {c}")
d = b**2-4*a*c
if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"есть 2 корня x1: {x1}, x2: {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"есть только один корень: {x}")
else:
    print("Кореней нет")