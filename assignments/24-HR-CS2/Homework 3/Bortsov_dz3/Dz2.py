import re
import math

uravnenije = input("Введите квадратное уравнение: ")
uravnenije  = uravnenije .replace(" ", "").lower()
pervChast = uravnenije.split("=")[0]
a = int(pervChast.split("x^2")[0] or 1)
ostatok = pervChast.split("x^2")[1]

b = int(ostatok.split("x")[0] or 1)
c = int(ostatok.split("x")[1] or 0)

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