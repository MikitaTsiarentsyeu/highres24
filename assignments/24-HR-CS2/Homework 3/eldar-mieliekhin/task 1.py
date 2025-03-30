import math

a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("No real roots")
else:
    sqrt_D = math.sqrt(D)
    x1 = (-b - sqrt_D) / (2 * a)
    x2 = (-b + sqrt_D) / (2 * a)
    print(f"First root: {x1}, Second root: {x2}")
