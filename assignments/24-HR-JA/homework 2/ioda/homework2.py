from decimal import Decimal
a = Decimal(input("Start number\n")) 
b = Decimal(input("Discount\n"))
c = Decimal(input("Invest Period\n"))
print("result:", a*(1+b/100)**c)