import math

print("Welcome to quadratic ecvasion solver")
print("Write A coef")
a = float(input())

print("Write B coef")
b = float(input())

print("Write C coef")
c = float(input())

D = (b ** 2) - 4 * a * c

if (D > 0):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    print(f"x1: {x1}")
    print(f"x2: {x2}")
elif(D == 0):
    x = -b / (2 * a)
    print(f"x: {x}")
else:
    print("no real roots")