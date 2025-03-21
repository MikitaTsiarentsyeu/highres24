# starting sum, interest rate, and investment period
from decimal import Decimal

print("Hello! Let's calculate your potential income, so what's your initial capital?")
capital = Decimal(input())

print("What's current interest rate?")
rate = (Decimal(input()) / 1200)
if rate < 1:
    rate += 1
print("What's the investment period in months?")
duration = int(input())
Potential = Decimal(capital * rate ** duration)
print("Congratulations! Your Total Earning potential is Potential is", Potential)
















