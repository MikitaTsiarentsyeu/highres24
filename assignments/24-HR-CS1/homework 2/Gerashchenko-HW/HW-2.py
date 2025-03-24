first_sum = float(input("Введите начальную сумму: "))
percent = float(input("Введите процентную ставку: "))
count_years = int(input("Введите кол-во лет: "))
result = first_sum * (1 + percent / 100) ** count_years
print("Итоговая сумма через " + str(count_years) + " лет: " + str(result))