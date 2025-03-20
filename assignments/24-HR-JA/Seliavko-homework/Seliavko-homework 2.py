import decimal

start_sum = decimal.Decimal(input("sum ($): "))
int_rate = decimal.Decimal(input("rate (%): "))
invest_period = decimal.Decimal(input("period of years: "))

final_amount = start_sum * (1 + int_rate / 100) ** invest_period

print(f"After {invest_period} years, your investment will be: ${final_amount:.2f}")
