import math
print("Enter the quadratic equation in the format ax^2 + bx + c = 0:")
equation = input()
try:
    equation = equation.replace(' ', '').replace('=0', '')
    a, b, c = equation.split('x^2')[0], equation.split('x^2')[1].split('x')[0], equation.split('x')[1]
    a, b, c = float(a), float(b), float(c)

    if a == 0:
        print("Fatal error: 'a' cannot be zero in a quadratic equation.")
    else:
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            x1 = (-b - math.sqrt(discriminant)) / (2 * a)
            x2 = (-b + math.sqrt(discriminant)) / (2 * a)
            print(f" roots: x1 = {x1}, x2 = {x2}")
        elif discriminant == 0:
            x = -b / (2 * a)
            print(f" root: x = {x}")
        else:
            print("No real roots.")
except ValueError:
    print("Error:")
