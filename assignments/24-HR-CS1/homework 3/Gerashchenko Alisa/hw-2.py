import math

expression = input("Enter the expression like this: 2x*x+3x+6=0: ").replace(" ", "").lower()[:-2]

a, b_с = expression.split("x*x")
b, c = b_с.split("x")
a = int(a)
b = int(b)
c = int(c)

if a == 0:
    print("a can't be zero!")
else:
    d = b ** 2 - 4 * a * c

    if d < 0:
        print("There are no roots")
    elif d == 0:
        x = -b // (2 * a)
        print("One real root: " + str(x))
    else:
        x1 = (-b + int(math.sqrt(d))) // (2 * a)
        x2 = (-b - int(math.sqrt(d))) // (2 * a)
        print("Two real roots: " + str(x1) + " and " + str(x2))