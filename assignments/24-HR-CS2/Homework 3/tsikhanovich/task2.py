import re

print("Enter the equation itself in form of ax*x+bx+c=0:")
equation = input("Enter equation: ")

match = re.match(r"([+-]?\d*\.?\d*)x\*x([+-]\d*\.?\d*)x([+-]\d*\.?\d*)=0", equation.replace(" ", ""))
if match:
    a = float(match.group(1) or "1")
    b = float(match.group(2))
    c = float(match.group(3))

    D = b * b - 4 * a * c
    print("D =", D)

    if D > 0:
        x1 = (-b + D ** 0.5) / (2 * a)
        x2 = (-b - D ** 0.5) / (2 * a)
        print("x1 =", x1, "x2 =", x2)
    elif D == 0:
        x = -b / (2 * a)
        print("x = ", x)
    else:
        print("No solutions")
else:
    print("Error")
