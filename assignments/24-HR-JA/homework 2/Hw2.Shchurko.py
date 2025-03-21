import decimal

startSum = decimal.Decimal(input("Enter the starting sum: ")).quantize(decimal.Decimal(".01"))
interestRate = decimal.Decimal(input("Enter interest rate per year (in %): ")) / 100
investmentPeriod = int(input("Enter the investment period in months: "))

finalSum = startSum * ((1 + interestRate / 12) ** investmentPeriod)

finalSum = finalSum.quantize(decimal.Decimal(".01"))

print("Final sum = ", finalSum)
