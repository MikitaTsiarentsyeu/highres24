import math
def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

while True:
    eq = input("Введите уравнение в виде ax*x+b*x+c=0 : ")
    eq = eq.replace(" ", "").replace("x", "").replace("*", "")
    if is_number(eq.split("+")[0]):
        a = float(eq.split("+")[0])
        if is_number(eq.split("+")[1]):
            b = float(eq.split("+")[1])
            if is_number(eq.split("+")[2].split("=")[0]):
                c = float(eq.split("+")[2].split("=")[0])
                break
            else:
                print("Выражение введено неправильно")
        else:
            print("Выражение введено неправильно")
    else:
        print("Выражение введено неправильно")
d = b**2-4*a*c
if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"Есть 2 корня x1: {x1}, x2: {x2}")
elif d == 0:
    x = -b / (2 * a)
    print(f"Есть только один корень: {x}")
else:
    print("Кореней нет")