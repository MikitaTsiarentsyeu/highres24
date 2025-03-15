from decimal import Decimal

s = Decimal(input("Start sum: "))
r = Decimal(input("Interest rate (percent per year): ")) / 100
t = Decimal(input("Investment period (years): "))
final = s * (1 + r) ** t
print(final)