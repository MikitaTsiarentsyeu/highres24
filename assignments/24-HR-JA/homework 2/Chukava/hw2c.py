from decimal import Decimal as decimal

x = decimal(input("Hole sum: "))
y = decimal(input("Procent: ")) / 100
z = decimal(input("Invest: "))
print("Summa: ", {sum * (y+1)**z})
