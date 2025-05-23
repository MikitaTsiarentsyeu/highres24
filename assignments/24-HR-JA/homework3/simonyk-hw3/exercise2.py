import re
import math

equation = input("Enter a quadratic equation in the form ax*x+bx+c=0: ")
equation = equation.replace(" ", "")
pattern = r'([-+]?[\d\.]*?)x\*x([-+]?[\d\.]+)x([-+]?[\d\.]+)=0'
match = re.match(pattern, equation)
if not match:
    print("Invalid equation format. Please enter in the form ax*x+bx+c=0")
else:
    a = float(match.group(1)) if match.group(1) else 1.0
    b = float(match.group(2))
    c = float(match.group(3))

    discriminant = (b ** 2) - (4 * a * c)

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Roots: {root1}, {root2}")
    elif discriminant == 0:
        root = -b / (2 * a)
        print(f"One root: {root}")
    else:
        print("Discriminant < 0, no roots exist")