#Write a program which will allow a user to enter coeffs a, b and c of some
# quadratic equation. Solve the equation and present results to the user
import math

a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("Coefficient 'a' cannot be zero.")
else:
    discriminant = b**2 - 4*a*c
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        print("Two roots:" , root1 , " " , root2)
    elif discriminant == 0:
        root = -b / (2*a)
        print("One root:", root)
    else:
        print("Discriminant < 0, I'm not doing that")
