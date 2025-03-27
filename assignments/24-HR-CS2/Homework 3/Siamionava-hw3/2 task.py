import math
import re

def QuadraticEquation (a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "no roots"
    
    if discriminant == 0:
        return -b / 2 * a
        
    if discriminant > 0:
        root1 = -b + math.sqrt(discriminant) / 2 * a
        root2 = -b - math.sqrt(discriminant) / 2 * a
        return root1, root2
    

def parse_equation(equation):
    equation = equation.replace(" ", "")
    pattern = r"([+-]?\d*\.?\d*)x\^2([+-]?\d*\.?\d*)x([+-]?\d*\.?\d*)=0"
    match = re.match(pattern, equation)
    
    if not match:
        raise ValueError("Invalid equation format. Please enter in the form ax^2+bx+c=0.")
    
    a, b, c = match.groups()

    a = float(a) if a else 1.0
    b = float(b) if b else 0.0
    c = float(c) if c else 0.0
    
    return a, b, c


equation = input("Enter the quadratic equation in the form ax^2+bx+c=0: ")

coeffs = parse_equation(equation)

a = coeffs[0]
b = coeffs[1]
c = coeffs[2]

result = QuadraticEquation(a, b, c)

if isinstance(result, tuple):
    print(f"The roots of the quadratic equation are: {result[0]} and {result[1]}")
else:
    print(f"The root of the quadratic equation is: {result}")