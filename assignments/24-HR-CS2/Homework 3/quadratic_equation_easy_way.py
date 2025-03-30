import math

def solve_quadratic(a: float, b: float, c: float) -> None | tuple[float] | tuple[float, float]:
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero")

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    if discriminant == 0:
        return -b / (2 * a),


try:
    a: float = float(input("Enter coefficient a: "))
    b: float = float(input("Enter coefficient b: "))
    c: float = float(input("Enter coefficient c: "))

    roots = solve_quadratic(a, b, c)

    if len(roots) == 2:
        print(f"The roots are: {roots[0]} and {roots[1]}")
    else:
        print(f"The root is: {roots[0]}")

except ValueError as e:
    print(f"Error: {e}")