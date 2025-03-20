print("Добро пожаловать в калькулятор инвестиций!")

starting_sum = float(input("Введите начальную сумму денег: "))

interest_rate = float(input("Введите годовую процентную ставку (например, 5 для 5%): "))

investment_period = int(input("Введите срок инвестирования в годах: "))

final_amount = starting_sum * (1 + interest_rate / 100) ** investment_period

print(f"Через {investment_period} лет ваша инвестиция вырастет до: {final_amount:.2f} рублей.")