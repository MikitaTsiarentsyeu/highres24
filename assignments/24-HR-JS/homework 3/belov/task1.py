import math

def solve_quadratic(a, b, c):
    if a == 0:
        print("This is not a quadratic equation.")
        return

    d = b**2 - 4*a*c

    if d > 0:
        root1 = (-b + math.sqrt(d)) / (2 * a)
        root2 = (-b - math.sqrt(d)) / (2 * a)
        return root1,root2
    elif d == 0:
        root = -b / (2 * a)
        return root,root
    else:
        return math.nan, math.nan

# User input
print("Enter the coefficients of the quadratic equation (ax^2 + bx + c = 0):")
a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

print(solve_quadratic(a, b, c))
