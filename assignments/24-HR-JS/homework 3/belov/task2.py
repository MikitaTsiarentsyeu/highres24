import re
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

def parse_equation(equation):

    match = re.match(r"(-?\d*\.?\d*)x\*x([+-]?\d*\.?\d*)x([+-]\d*\.?\d*)=0", equation)
    if not match:
        print("Invalid format! Please ensure the equation is in the form 'ax*x+bx+c=0'")
        return False, False, False

    a = float(match.group(1) or "1")
    b = float(match.group(2) or "1")
    c = float(match.group(3) or "0")
    return a, b, c


equation = input("Enter a quadratic equation in the form 'ax*x+bx+c=0':")
a, b, c = parse_equation(equation)
print(solve_quadratic(a, b, c))
