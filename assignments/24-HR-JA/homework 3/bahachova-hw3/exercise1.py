import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
discriminant = (b ** 2) - (4 * a * c)

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1}, {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"One root: {root}")
else:
    print("Discriminant < 0, no roots exist")