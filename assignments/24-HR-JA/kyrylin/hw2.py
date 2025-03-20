firstSum = float(input("Enter the initial amount:"))
firstRate = float(input("Enter the annual interest rate:"))
yourTerm = int(input("Enter the investment term:"))

finalSum = firstSum * (1 + firstRate/100) ** yourTerm
print(f"\nIn {yourTerm} years your amount will be: {finalSum} ")