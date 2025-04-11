import decimal
import math

a = decimal.Decimal(input("a coefficient: "))
b = decimal.Decimal(input("b coefficient: "))
c = decimal.Decimal(input("c coefficient: "))
D = b ** 2 - 4 * a * c
if D > 0:
    print(round((decimal.Decimal(math.sqrt(D)) - b) / (2 * a), 3), round((-(decimal.Decimal(math.sqrt(D))) - b) / (2 * a), 3))
elif D == 0:
    print(round((-b) / (2 * a), 3))
else:
    print("No roots")