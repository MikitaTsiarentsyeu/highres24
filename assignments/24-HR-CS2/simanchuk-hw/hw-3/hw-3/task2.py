from decimal import Decimal as D
from calculate import solvEquation


print("Write a equation like this: ax**2+bx+c=0")
equation = input("Enter here: ")

parseEquation = equation.replace(" ", "").replace("=0","")
newParse = parseEquation.replace("x**2"," ").replace("x"," ")
coeff = newParse.split()


a, b, c = map(D, coeff)
    
roots = solvEquation(a, b, c)

if isinstance(roots, tuple):
    print(f"Roots: {', '.join(map(str, roots))}")
else:
    print(f"Roots: {roots}")