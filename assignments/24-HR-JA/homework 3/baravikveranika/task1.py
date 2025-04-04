import math

a = float(input("Enter the a: "))
b = float(input("Enter the b: "))
c = float(input("Enter the c: "))

d = b**2 - 4*a*c
if d < 0:
    print("No roots")
elif d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Two roots:", x1, x2)
elif d == 0:
    x = -b / (2 * a)
    print("One root:", x)

