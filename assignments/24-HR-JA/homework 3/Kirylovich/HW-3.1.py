import math

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

D = b**2 - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"Уравнение имеет два корня: x1 = {x1} и x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"Уравнение имеет один корень: x = {x}")
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-D) / (2 * a)
    print(f"Уравнение имеет два комплексных корня: x1 = {realPart} + {imaginaryPart}i и x2 = {realPart} - {imaginaryPart}i")

