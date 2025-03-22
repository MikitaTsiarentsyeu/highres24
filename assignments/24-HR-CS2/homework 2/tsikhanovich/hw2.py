from decimal import Decimal
num1 = Decimal(input("Starting sum:")) 
num2 = Decimal(input("Interest rate:"))
num3 = Decimal(input("Investment period:"))
print("Potential money income:", num1*(1+num2/100)**num3)
