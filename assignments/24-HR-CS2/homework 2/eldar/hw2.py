from decimal import Decimal

startMoney = Decimal(input("Start money: "))
rate = Decimal(input("Rate: "))
period = Decimal(input("Period: "))
income = startMoney * (1 + rate / 100) ** period - startMoney
print(f"Your income: {income}")
