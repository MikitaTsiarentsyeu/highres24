from calculate_income import calculate_income

print("Investment Income Calculator")
try:
    principal = float(input("Enter the initial investment amount: "))
    rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the number of years: "))

    final_amount = calculate_income(principal, rate, years)
    print(f"Potential income after {years} years: {final_amount:.2f}")
except ValueError:
    print("Invalid input")
