from decimal import Decimal


startSum = Decimal(input("Input the starting sum: "))
inteRate = Decimal(input("Input the interest rate(%): ")) / 100
invPer = Decimal(input("Input the investment period: "))
result = startSum * ((inteRate + 1) ** invPer)

print(f'With all your values, you will get: {result:.2f}')
