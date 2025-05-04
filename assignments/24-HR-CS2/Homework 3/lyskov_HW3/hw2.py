from decimal import Decimal as D
from calculate import solvEquation

print("Write an equation like this: ax**2+bx+c=0")
equation = input("Enter here: ")

equation = equation.replace(" ", "")  
equation = equation.replace("=0", "")  

equation = equation.replace("x**2", " ")
equation = equation.replace("x", " ")

parts = equation.split()

a = D(parts[0])
b = D(parts[1])
c = D(parts[2])

roots = solvEquation(a, b, c)

if type(roots) == tuple:
    print("Roots:", str(roots[0]) + ", " + str(roots[1]))
else:
    print("Roots:", roots)
