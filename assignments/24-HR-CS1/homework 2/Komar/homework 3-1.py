import math

while True:
    a = float(input("Enter a: "))
    if a == 0:
        print("a can't be zero")
    else:
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        break

discriminant = b ** 2 - 4 * a * c
if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2 * a)
    root2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Roots: {root1} and {root2}")
elif discriminant == 0:
    root = -b / (2 * a)
    print(f"Root: {root}")
else:
    print("There are no real roots")
