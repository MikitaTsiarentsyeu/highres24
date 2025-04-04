import math
import re

def coefficients(equation):
    match = re.match(r'(-?\d*)x\^2([+-]?\d*)x([+-]?\d*)=0', equation.replace(" ", ""))
    if not match:
        raise ValueError("Incorrect equation format")
    a = int(match.group(1)) if match.group(1) != "" else 1
    b = int(match.group(2)) if match.group(2) != "" else 1
    c = int(match.group(3)) if match.group(3) != "" else 0
    return a, b, c

equation = input("Enter equation (Example: x^2 + 3x + 2 = 0): ")
a, b, c = coefficients(equation)

if a == 0:
    print("No solution")
else:
    D = b**2 - 4*a*c
    if D < 0:
        print("No solution")
    elif D == 0:
        x = -b / (2*a)
        print(f"solution: x = {x}")
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        print(f"solutions: x1 = {x1}, x2 = {x2}")