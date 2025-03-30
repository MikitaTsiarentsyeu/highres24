import re
from quadratic_equation_easy_way import solve_quadratic


def extract_coefficients(equation: str) -> tuple[float, float, float]:
    equation = equation.replace(" ", "").lower()

    pattern = r"([+-]?\d*)x\^2([+-]?\d*)x([+-]?\d*)=0"
    match = re.match(pattern, equation)

    if not match:
        raise ValueError("Invalid format")

    a_str, b_str, c_str = match.groups()

    a = float(a_str) if a_str not in ["", "+"] else 1.0 if a_str == "+" else -1.0 if a_str == "-" else 1.0
    b = float(b_str) if b_str not in ["", "+"] else 1.0 if b_str == "+" else -1.0 if b_str == "-" else 1.0
    c = float(c_str) if c_str else 0.0

    return a, b, c


try:
    equation = input("Enter the quadratic equation")

    a, b, c = extract_coefficients(equation)
    print(f"Extracted coefficients: a = {a}, b = {b}, c = {c}")

    roots = solve_quadratic(a, b, c)

    if len(roots) == 2:
        print(f"The roots are: {roots[0]} and {roots[1]}")
    else:
        print(f"The root is: {roots[0]}")

except ValueError as e:
    print(f"Error: {e}")