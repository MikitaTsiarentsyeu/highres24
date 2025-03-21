from decimal import Decimal
a = Decimal(input("write starting sum\n"))
b = Decimal(input("write interest rate\n"))
c = Decimal(input("write investment period\n"))
print("result:", a * (1 + b / 100) ** c)