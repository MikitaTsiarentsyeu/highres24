import math

a, b, c = float(input("a: ")), float(input("b: ")), float(input("c: "))

if a == 0:
    print("not a quadratic equation")
else:
    d = b**2 - 4*a*c  
    if d > 0:
        print("root:", (-b + math.sqrt(d)) / (2*a), (-b - math.sqrt(d)) / (2*a))
    elif d == 0:
        print("root:", -b / (2*a))
    else:
        print("root:", complex(-b / (2*a), math.sqrt(-d) / (2*a)), complex(-b / (2*a), -math.sqrt(-d) / (2*a)))
