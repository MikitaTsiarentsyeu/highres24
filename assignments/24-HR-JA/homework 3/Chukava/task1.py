import math

a = float(input())
b = float(input())
c = float(input())

if a == 0:
    pass
else:
    d = b**2 - 4*a*c

    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2*a)
        x2 = (-b - math.sqrt(d)) / (2*a)
        print(x1, x2)
    elif d == 0:
        x = -b / (2*a)
        print(x)
    else:
        print("no solution")