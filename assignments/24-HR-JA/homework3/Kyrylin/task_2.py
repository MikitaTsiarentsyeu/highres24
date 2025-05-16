import re
import math

user_input = input("Enter a quadratic equation in the form ax*x+bx+c=0: ").replace(" ", "")
pattern = r'([-+]?\d*\.?\d*)x\*x([-+]?\d*\.?\d*)x([-+]?\d*\.?\d*)=0'
match = re.match(pattern, user_input)

if not match:
    print("Invalid equation format. Please use: ax*x+bx+c=0")
else:
    a_str = match.group(1)
    a = float(a_str) if a_str not in ("", "+", "-") else float(a_str + "1") if a_str else 1.0

    b_str = match.group(2)
    b = float(b_str) if b_str not in ("", "+", "-") else float(b_str + "1") if b_str else 1.0

    c = float(match.group(3))

    D = b ** 2 - 4 * a * c
    if D > 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        print(f"Two real roots: x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = -b / (2 * a)
        print(f"One real root: x = {x}")
    else:
        print("No real roots (discriminant < 0)")
