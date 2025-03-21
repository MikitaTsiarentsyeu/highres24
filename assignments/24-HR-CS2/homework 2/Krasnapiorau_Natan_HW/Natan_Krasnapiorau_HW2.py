import math
import decimal
from decimal import Decimal

def CalculateIncome():
    while True:

        startingSum = Decimal((input("Enter the amount of money you want put on interest (in $): ")))
        interestRate = Decimal((input("Enter the annual interest rate (in %): ")))
        investmentPeriodYear = int((input("Enter the number of years: ")))

        endIncome = round((startingSum * ((1 + interestRate / 100) ** investmentPeriodYear)), 2)
        print(f"After {investmentPeriodYear} years you will get {endIncome}$")

        userInput = input(f"Do you want to put {startingSum}$ for {investmentPeriodYear} years at interest rate of {interestRate}%? y/n ")
        if userInput == "y":
            break
    print("Thank you for choosing us")        

CalculateIncome()    