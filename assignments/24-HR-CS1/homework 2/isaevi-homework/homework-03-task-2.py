import math

z = input("Please enter quadratic equation (for example: 2x^2+3x-5=0): ").replace(" ", "").replace("=0", "")
a, b, c = map(float, z.replace("x^2", " ").replace("x", " ").replace("+-", "-").replace("--", "- -").split())

d = b**2 - 4 * a * c

if d >= 0:
    print("root:", (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a) if d else -b / (2 * a))
else:
    print("complex root:", complex(-b / (2 * a), math.sqrt(-d)/(2*a)), complex(-b / (2 * a), -math.sqrt(-d)/(2 * a)))
