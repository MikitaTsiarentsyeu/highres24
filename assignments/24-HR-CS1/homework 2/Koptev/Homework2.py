from decimal import Decimal
startNum = Decimal(input("Enter a start number: "))
interestRate = Decimal(input("Enter an interest rate (%): ")) / 100
period = Decimal(input("Enter a period (year): "))
income = startNum * interestRate * period
print("The income is:", income)