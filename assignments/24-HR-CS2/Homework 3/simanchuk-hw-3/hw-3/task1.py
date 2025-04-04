from decimal import Decimal as D
from calculate import solvEquation


print("Write a, b and c for ax^2 + bx + c = 0: \n")
a = D(input("A: "))
b = D(input("B: "))
c = D(input("C: "))

roots = solvEquation(a, b, c)

if isinstance(roots, tuple):
    print(f"Roots: {', '.join(map(str, roots))}")
else:
    print(f"Roots: {roots}")