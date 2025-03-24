initial_sum = float(input("Enter your starting sum: "))
interest_rate = float(input("Enter your interest rate: "))
period = int(input("Enter your investment period: "))
res = initial_sum * (interest_rate/100+1)**period
print("Final amount: ", res)