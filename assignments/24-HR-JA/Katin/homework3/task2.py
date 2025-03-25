import decimal
import math

stringEquation = input("input your equation (form: ax\\x+bx+c=0):")
modifiedString = stringEquation.replace("x\\x", ",").replace("x", ",").replace("=0", "")
arrayOfNumbers = modifiedString.split(",")
a = decimal.Decimal(arrayOfNumbers[0])
b = decimal.Decimal(arrayOfNumbers[1])
c = decimal.Decimal(arrayOfNumbers[2])
D = b ** 2 - 4 * a * c
if D > 0:
    print(round((decimal.Decimal(math.sqrt(D)) - b) / (2 * a), 3), round((-(decimal.Decimal(math.sqrt(D))) - b) / (2 * a), 3))
elif D == 0:
    print(round((-b) / (2 * a), 3))
else:
    print("No roots")







