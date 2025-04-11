# Quadratic Equation Solver
import math

print("Quadratic Equation Solver (ax² + bx + c = 0)")

try:
    a = float(input("Enter coefficient a: "))
    if a == 0:
        print("Error: 'a' cannot be zero for a quadratic equation")
        exit()
        
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))

    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        sqrt_d = math.sqrt(discriminant)
        root1 = (-b + sqrt_d) / (2*a)
        root2 = (-b - sqrt_d) / (2*a)
        print(f"Two distinct real roots: {root1:.2f} and {root2:.2f}")
        
    elif discriminant == 0:
        root = -b / (2*a)
        print(f"One real root (repeated): {root:.2f}")
        
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"Two complex roots: {real_part:.2f} + {imaginary_part:.2f}i and {real_part:.2f} - {imaginary_part:.2f}i")

except ValueError:
    print("Error: Please enter valid numbers for coefficients")