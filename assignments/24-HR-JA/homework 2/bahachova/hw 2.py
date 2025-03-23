from decimal import Decimal as decimal
sum = decimal(input("Input sum: "))
proc = decimal(input("Input proc: ")) / 100
invest = decimal(input("Input invest: "))
print(f"Final sum is: {sum * (proc+1)**invest}")