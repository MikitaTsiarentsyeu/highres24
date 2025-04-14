import math

def parse_quadratic_equation(equation):
    equation = equation.replace(' ', '')
    if not equation.endswith('=0'):
        raise ValueError("Equation must end with '=0'")

    equation = equation[:-2]  # remove '=0'

    # Replace all '-' with '+-' to simplify splitting
    equation = equation.replace('-', '+-')
    terms = equation.split('+')

    a = b = c = 0
    for term in terms:
        if not term:
            continue
        if 'x*x' in term:
            coeff = term.replace('x*x', '')
            a = float(coeff) if coeff not in ('', '+', '-') else float(coeff + '1')
        elif 'x' in term:
            coeff = term.replace('x', '')
            b = float(coeff) if coeff not in ('', '+', '-') else float(coeff + '1')
        else:
            c = float(term)

    return a, b, c

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("The coefficient 'a' cannot be zero for a quadratic equation.")

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two real roots: {root1}, {root2}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One real root: {root}"
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Two complex roots: {real_part} ± {imaginary_part}i"

def main():
    equation = input("Enter a quadratic equation in the form ax*x + bx + c = 0: ")
    try:
        a, b, c = parse_quadratic_equation(equation)
        result = solve_quadratic(a, b, c)
        print(result)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
