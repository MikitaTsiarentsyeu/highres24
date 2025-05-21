while True:
    print("Выберите операцию: \n1 - Деление\n2 - Умножение\n3 - Вычитание\n4 - Сложение\n0 - Выход")
    op = input("Введите номер операции: ")

    if op == "0":
        print("Выход")
        break

    if op in ["1", "2", "3", "4"]:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Некорректно введено число")
            continue

        if op == "1":
            if b == 0:
                print("На ноль делить нельзя")
            else:
                print("Результат:", a / b)
        elif op == "2":
            print("Результат:", a * b)
        elif op == "3":
            print("Результат:", a - b)
        elif op == "4":
            print("Результат:", a + b)
    else:
        print("Неправильная операция")
