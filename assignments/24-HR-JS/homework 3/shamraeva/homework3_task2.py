import re
import math

def parse_equation(equation):
    equation = equation.replace(" ", "").replace("=0", "")
    pattern = r'(?P<a>[-+]?\d*)x\*x(?P<sign_b>[-+])(?P<b>\d*)x(?P<sign_c>[-+])(?P<c>\d+)'
    match = re.match(pattern, equation)

    if not match:
        raise ValueError("Invalid format")

    a = int(match.group("a")) if match.group("a") not in ("", "+", "-") else int(match.group("a")+"1")
    b = int(match.group("b")) if match.group("b") else 1
    c = int(match.group("c"))

    if match.group("sign_b") == "-":
        b = -b
    if match.group("sign_c") == "-":
        c = -c

    return a, b, c

def main():
    try:
        equation = input("Enter equation: ")
        a, b, c = parse_equation(equation)

        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print(f"Two roots: x1 = {x1}, x2 = {x2}")
        elif d == 0:
            x = -b / (2*a)
            print(f"One root: x = {x}")
        else:
            print("No real roots")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()