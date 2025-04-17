import math
import re

equation = input("Введите квадратное уравнение: ")

equation = equation.replace(" ", "")

pattern = r"([+-]?\d*\.?\d*)x\*x([+-]?\d*\.?\d*)x([+-]?\d*\.?\d*)=0"
match = re.match(pattern, equation)

if not match:
    raise ValueError("Неверный формат. Введите в формате ax^2+bx+c=0")

a, b, c = match.groups()

a = float(a) if a else 1.0
b = float(b) if b else 0.0
c = float(c) if c else 0.0

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Уравнение имеет 2 корня: x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"Уравнение имеет один корень: {x}")
else:
    print("Данное уравнение не имеет корней")
