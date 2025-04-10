def calculate_income(principal, rate, years):
    return principal * (1 + rate / 100) ** years

def main():
    print("Investment Income Calculator")

    try:
        amount = input("Enter the starting sum ($): ")
        rate = input("Enter the annual interest rate (%): ")
        period = input("Enter the investment period (in years): ")

        principal = float(amount)
        interest = float(rate)
        years = int(period)

        total = calculate_income(principal, interest, years)
        profit = total - principal

        print(f"\nAfter {years} years, your investment will grow to ${total:,.2f}")
        print(f"Total profit: ${profit:,.2f}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
