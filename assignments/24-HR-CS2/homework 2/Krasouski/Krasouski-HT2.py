from decimal import Decimal

print("What is the starting sum?")
start = input()

print("What is income rate?")
rate = Decimal(input()) / 100

print("What is the period of investment?")
time = input()

result = Decimal(start) * (1 + rate) ** Decimal(time)

print("result is ", result)