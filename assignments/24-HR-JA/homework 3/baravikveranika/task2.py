import re

print("Enter a quadratic equation in the form ax*x+bx+c=0 (example: 1x*x+1x-1=0):")
equation = input("Enter your equation: ")

match = re.match(r"([+-]?\d*\.?\d*)x\*x([+-]\d*\.?\d*)x([+-]\d*\.?\d*)=0", equation.replace(" ", ""))
if match:
    a = float(match.group(1) or "1")
    b = float(match.group(2))
    c = float(match.group(3))

    d = b * b - 4 * a * c
    print("Discriminant d =", d)

    if d > 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        print("The equation has two solutions: x1 =", x1, "and x2 =", x2)
    elif d == 0:
        x = -b / (2 * a)
        print("The equation has one solution: x = ", x)
    else:
        print("The equation has no real solutions")
else:
    print("Invalid input. Please enter the equation in the correct form: ax*x+bx+c=0")

