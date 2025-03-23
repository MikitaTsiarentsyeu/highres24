import math

equation = input("Enter the quadratic equation like this: ax*x+bx+c=0: ").replace(" ", "").lower()
try:
    parts = equation[:-2]
    ax_part, bxc_parts = parts.split("x*x")
    a = float(ax_part)
    bx_part, c_part = bxc_parts.split("x")
    b = float(bx_part)
    c = float(c_part)

    if a == 0:
        print("a can't be zero")
    else:
        discriminant = b ** 2 - 4 * a * c
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            print(f"Roots: {root1} and {root2}")
        elif discriminant == 0:
            root = -b / (2 * a)
            print(f"Root: {root}")
        else:
            print("There are no real roots")
except ValueError:
    print("Invalid equation format. Please enter in the form ax*x+bx+c=0.")
