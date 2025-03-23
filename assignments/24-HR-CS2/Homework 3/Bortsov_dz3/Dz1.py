import math

a = int(input("Введите коэффициент a: "))
b = int(input("Введите коэффициент b: "))
c = int(input("Введите коэффициент c: "))



deskriminant = b**2 - 4*a*c
if deskriminant > 0:
    x1 = (-b + math.sqrt(deskriminant)) / (2 * a)
    x2 = (-b - math.sqrt(deskriminant)) / (2 * a)
    print(f"Уравнение имеет 2 корня: x1 = {x1}, x2 = {x2}")
elif deskriminant == 0:
    x = -b / (2 * a)
    print(f"Уранение имеет один корень: {x}")
else:
    print("Данное уравнение не имеет корней")
