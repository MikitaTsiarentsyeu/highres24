import math

def QuadraticEquation (a: float, b: float, c: float):
    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return "no roots"
    
    if discriminant == 0:
        return -b / 2 * a
        
    if discriminant > 0:
        root1 = -b + math.sqrt(discriminant) / 2 * a
        root2 = -b - math.sqrt(discriminant) / 2 * a
        return root1, root2
    
a = float(input("write a coeff 'a'\n"))
b = float(input("write a coeff 'b'\n"))
c = float(input("write a coeff 'c'\n"))

result = QuadraticEquation(a, b, c)

if isinstance(result, tuple):
    print(f"The roots of the quadratic equation are: {result[0]} and {result[1]}")
else:
    print(f"The root of the quadratic equation is: {result}")