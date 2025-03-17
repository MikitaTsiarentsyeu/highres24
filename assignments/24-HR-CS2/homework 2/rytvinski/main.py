def calculate(starting_sum, rate, period_in_years):
    return starting_sum * (1 + rate / 100) * period_in_years


print("Income Calculator")
try:
    starting_sum = float(input("Enter your starting money amount: "))
    rate = float(input("Enter the interest rate (%): "))
    period = int(input("Enter the number of years: "))
    
    result = calculate(starting_sum, rate, period) - starting_sum;
    
    print(f"Income after {period} years is {round(result, 2)}")
except ValueError:
    print("Incorrect input")
    




