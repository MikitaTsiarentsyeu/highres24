startNum = float(input("Enter a start number: "))
interestRate = float(input("Enter an interest rate (%): ")) / 100
period = float(input("Enter a period (year): "))
income = startNum * interestRate * period
print("The income is:", income)