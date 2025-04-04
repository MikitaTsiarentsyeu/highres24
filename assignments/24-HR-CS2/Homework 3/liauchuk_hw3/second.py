import math
import re
def parse_quadratic(expression):
    expression = expression.replace(" ", "").lower()
    match = re.match(r'([-+]?\d*)x\^2([-+]?\d*)x([-+]?\d+)?', expression)
    
    if not match:
        raise ValueError("incorrect format")
    a = int(match.group(1)) if match.group(1) not in ("", "+", "-") else 1 if match.group(1) != "-" else -1
    b = int(match.group(2)) if match.group(2) not in ("", "+", "-") else 1 if match.group(2) != "-" else -1
    c = int(match.group(3)) if match.group(3) else 0
    
    return a, b, c

def solve(expression):
    try:
        a, b, c = parse_quadratic(expression)
    except ValueError as e:
        print(e)
        return
    
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"x = {x}")
    else:
        print("no roots")


equation = input("enter (ax^2+bx+c) where a,b,c are digits: ")
solve(equation)