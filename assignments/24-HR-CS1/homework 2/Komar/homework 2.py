initial_investment = float(input("Enter the starting sum: "))
rate = float(input("Enter the %: "))
time = int(input("Enter the investment period (in years): "))
final_amount = initial_investment * (1 + rate / 100) ** time
print(f"After {time} years, your investment will be worth: ${final_amount:.2f}")
