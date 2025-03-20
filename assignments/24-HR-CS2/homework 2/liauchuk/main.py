from decimal import Decimal

sum = Decimal(input("sum: "))
rate = Decimal(input("rate: ")) / 100
period = Decimal(input("period: "))
res = sum * ((rate + 1) ** period)

print('result:', round(res))