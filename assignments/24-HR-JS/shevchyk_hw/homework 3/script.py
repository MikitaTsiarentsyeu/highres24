import math


def solve_quadratic_easy():
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

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
    solve_quadratic_easy()
