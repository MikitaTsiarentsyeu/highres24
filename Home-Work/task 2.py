from decimal import Decimal
start = float(input("Initial capital: "))
rate = float(input("Annual interest rate (%): "))
period = int(input("Investment period (years): "))
result = start * (1 + rate / 100) ** period
print("Final amount:", result)