import re
import math

def parse_quadratic_equation(equation):
    equation = equation.replace(" ", "")

    if not equation.endswith("=0"):
        raise ValueError("Equation must be in the form ax^2 + bx + c = 0")

    pattern = r"([+-]?\d*)x\^2|([+-]?\d*)x|([+-]?\d+)(?=[+-]|$)"
    matches = re.findall(pattern, equation.split("=")[0])
    
    a, b, c = 0, 0, 0 
    
    for match in matches:
        if match[0]:
            coeff = match[0].replace("+", "")
            if coeff == "-":
                a = -1
            elif coeff == "":
                a = 1
            else:
                a = float(coeff)

        elif match[1]:
            coeff = match[1].replace("+", "")
            if coeff == "-":
                b = -1
            elif coeff == "":
                b = 1
            else:
                b = float(coeff)

        elif match[2]:
            c = float(match[2])
    
    return a, b, c

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return f"Two real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2*a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2*a)
        imag_part = math.sqrt(abs(discriminant)) / (2*a)
        return f"Two complex roots: {real_part} + {imag_part}i, {real_part} - {imag_part}i"

print("Quadratic Equation Solver (Hard Way)")
print("Enter an equation in the form: ax^2 + bx + c = 0")

equation = input("Enter the equation: ").strip()

try:
    a, b, c = parse_quadratic_equation(equation)
    print(f"\nParsed coefficients: a = {a}, b = {b}, c = {c}")
    
    if a == 0:
        print("This is not a quadratic equation (a = 0).")
    else:
        solution = solve_quadratic(a, b, c)
        print("Solution:", solution)
except ValueError as e:
    print("Error:", e)