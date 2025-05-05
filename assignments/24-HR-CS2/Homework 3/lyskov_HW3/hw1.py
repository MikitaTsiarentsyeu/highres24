from decimal import Decimal
from calculate import solvEquation

print("Введите коэффициенты уравнения ax^2 + bx + c = 0:\n")

a = Decimal(input("A: "))
b = Decimal(input("B: "))
c = Decimal(input("C: "))

result = solvEquation(a, b, c)

if type(result) == tuple:
    print("Корни уравнения:", str(result[0]) + ", " + str(result[1]))
else:
    print("Корни уравнения:", result)
