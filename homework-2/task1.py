startNum = int(input("Enter a start number: "))
interestRate = int(input("Enter an interest rate (%): ")) / 100
period = int(input("Enter a period (year): "))
income = startNum * interestRate * period
print("The income is:", income)
#EgorKoptev