#Write a program which will allow a user to enter the equation itself in form of ax*x+bx+c=0 of some quadratic equation.
# Solve the equation and present results to the user
import math

equation = input("Enter a quadratic equation that looks like that: ax*x+bx+c=0: ").replace(" ", "").replace("=0", "")
parts = equation.split("x*x")
a = int(parts[0])
rest = parts[1].split("x")
b = int(rest[0])
c = int(rest[1])
D = b**2 - 4*a*c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Roots are:", x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print("Root is:", x)
else:
    print("Nah i dont work with imaginary")