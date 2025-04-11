import decimal

startSum = decimal.Decimal(input("Enter starting sum: "))
percentageRate = decimal.Decimal(input("Enter percentage rate: "))
periodOfTime = decimal.Decimal(input("Enter period of time (in years): "))
resultSum = startSum * (1 + percentageRate / 100) ** periodOfTime;
print(f"From {startSum} with {percentageRate}% in {periodOfTime} years you will have {round(resultSum, 2)}")