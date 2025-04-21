import math

a = float(input("Enter coeff a: "))
b = float(input("Enter coeff b: "))
c = float(input("Enter coeff c: "))

D = math.pow(b, 2) - 4*a*c

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print(f"x1 = {x1}, x2 = {x2}")
elif D == 0:
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    realPart = -b / (2 * a)
    imaginaryPart = math.sqrt(-D) / (2 * a)
    print(f"x1 = {realPart} + {imaginaryPart}i и x2 = {realPart} - {imaginaryPart}i")
