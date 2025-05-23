while True:
    print("Виберите операцию: \n1 - Деления\n2 - Умножения\n3 - Вичитания\n4 - Добавления\n0 - Выход")
    op = input()
    match op:
        case "1":
            try:
                a = float(input("Ведите первое число: "))
                b = float(input("Ведите второе число: "))
                if b == 0:
                    print("На ноль делить нельзя")
                else:
                    print(a / b)
            except ValueError:
                print("Некоректно указано число")
        case "1":
            try:
                a = float(input("Ведите первое число: "))
                b = float(input("Ведите второе число: "))
                print(a * b)
            except ValueError:
                print("Некоректно указано число")
        case "1":
            try:
                a = float(input("Ведите первое число: "))
                b = float(input("Ведите второе число: "))
                print(a - b)
            except ValueError:
                print("Некоректно указано число")
        case "1":
            try:
                a = float(input("Ведите первое число: "))
                b = float(input("Ведите второе число: "))
                print(a + b)
            except ValueError:
                print("Некоректно указано число")
        case "1":
            print("Выход")
            exit()
        case _:
            print("Неправильная операция")