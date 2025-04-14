import decimal

startSum = decimal.Decimal(input("Enter the initial amount:"))
interestRate = decimal.Decimal(input("Enter the interest rate:"))
investmentPeriod = decimal.Decimal(input("Enter the investment period:"))
print("result:", startSum * (interestRate + 1) ** interestRate) 