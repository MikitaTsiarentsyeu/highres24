import math

print("Quadratic Equation Solver")
print("Equation format: ax² + bx + c = 0")

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

discriminant = b**2 - 4*a*c

if discriminant > 0:
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Distinct roots: {root1:.2f} and {root2:.2f}")
elif discriminant == 0:
    root = -b / (2*a)
    print(f"One real root: {root:.2f}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"Complex roots: {real_part:.2f} ± {imaginary_part:.2f}i")