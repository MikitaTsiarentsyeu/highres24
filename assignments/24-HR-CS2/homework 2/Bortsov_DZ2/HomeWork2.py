sum = float(input("сумма:  "))
proc =float(input(("процент: ")))/100
invest = float(input(("инвестиция: ")))
print(f"итоговая сумма: {sum * (proc + 1)**invest}")