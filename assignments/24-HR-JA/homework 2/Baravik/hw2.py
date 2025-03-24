from decimal import Decimal as decimal
sum = decimal(input("sum: "))
proc = decimal(input("proc: ")) / 100
invest = decimal(input("invest: "))
print(f"final sum: {sum * (proc+1)**invest}")