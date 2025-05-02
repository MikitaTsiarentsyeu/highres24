import math

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

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