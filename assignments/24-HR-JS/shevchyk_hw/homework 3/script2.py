import re
import math


def solve_quadratic_hard():
    equation = input("Enter a quadratic equation in form ax^2+bx+c=0: ")

    match = re.match(r'([-\d.]+)x\^2([+-]\d+.?)x([+-]\d+.?)=0', equation.replace(" ", ""))
    if not match:
        print("Invalid format.")
        return

    a, b, c = map(float, match.groups())
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("No real roots.")
    elif discriminant == 0:
        x = -b / (2 * a)
        print(f"One root: {x}")
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print(f"Two roots: {x1}, {x2}")


if __name__ == "__main__":
    solve_quadratic_hard()