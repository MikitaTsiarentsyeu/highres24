starting_sum = float(input("Введите начальную сумму: "))  
interest_rate = float(input("Введите ставку процентов (в процентах): "))  
investment_period = float(input("Введите период инвестирования (в годах): "))  

interest_rate_decimal = interest_rate / 100  

resulting_sum = starting_sum * ((1 + interest_rate_decimal) ** investment_period)  

print(f"По окончании {investment_period} лет, со ставкой процентов {interest_rate}%, у вас будет {resulting_sum:.2f}")  