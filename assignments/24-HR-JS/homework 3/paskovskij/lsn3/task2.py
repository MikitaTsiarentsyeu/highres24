print("Enter the coefficients of the quadratic equation (ax^2 + bx + c = 0):")
eques = input().split("+")
a = int(eques[0].split("x^2")[0])
b = int(eques[1].split("x")[0])
c = int(eques[2].split("=")[0])
if a == 0:
        print("This is not a quadratic equation.")
else:
        D = b**2 - 4*a*c
        if D > 0:
                x1 = (-b + D**0.5) / (2*a)
                x2 = (-b - D**0.5) / (2*a)
                print(f"The roots are {x1} and {x2}.")
        elif D == 0:
                x = -b / (2*a)
                print(f"The root is {x}.")
        else:
                print("The equation has no real roots.")