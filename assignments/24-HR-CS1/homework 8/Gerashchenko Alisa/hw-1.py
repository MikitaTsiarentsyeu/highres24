import math

while True:
    print("\nВыберите операцию:")
    print("1 - Сложение")
    print("2 - Вычитание")
    print("3 - Деление")
    print("4 - Умножение")
    print("5 - Целочисленное деление")
    print("6 - Возведение в степень")
    print("7 - Извлечение квадратного корня")
    print("8 - Остаток от деления")
    print("0 - Выход")

    oper = input("Введите номер операции: ")

    match oper:
        case "1":
            try:
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                print("Результат:", a + b)
            except ValueError:
                print("Ошибка: некорректный ввод числа.")
        case "2":
            try:
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                print("Результат:", a - b)
            except ValueError:
                print("Ошибка: некорректный ввод числа.")
        case "3":
            try:
                a = float(input("Делимое: "))
                b = float(input("Делитель: "))
                if b == 0:
                    print("Ошибка: деление на ноль.")
                else:
                    print("Результат:", a / b)
            except ValueError:
                print("Ошибка: некорректный ввод числа.")
        case "4":
            try:
                a = float(input("Первое число: "))
                b = float(input("Второе число: "))
                print("Результат:", a * b)
            except ValueError:
                print("Ошибка: некорректный ввод числа.")
        case "5":
            try:
                a = int(input("Делимое (целое число): "))
                b = int(input("Делитель (целое число): "))
                if b == 0:
                    print("Ошибка: деление на ноль.")
                else:
                    print("Результат:", a // b)
            except ValueError:
                print("Ошибка: введите целые числа.")
        case "6":
            try:
                a = float(input("Основание: "))
                b = float(input("Степень: "))
                print("Результат:", a ** b)
            except ValueError:
                print("Ошибка: некорректный ввод числа.")
        case "7":
            try:
                a = float(input("Число: "))
                if a < 0:
                    print("Ошибка: нельзя извлечь корень из отрицательного числа.")
                else:
                    print("Результат:", math.sqrt(a))
            except ValueError:
                print("Ошибка: некорректный ввод числа.")
        case "8":
            try:
                a = int(input("Делимое (целое число): "))
                b = int(input("Делитель (целое число): "))
                if b == 0:
                    print("Ошибка: деление на ноль.")
                else:
                    print("Результат:", a % b)
            except ValueError:
                print("Ошибка: введите целые числа.")
        case "0":
            print("Выход из программы.")
            break
        case _:
            print("Ошибка: неизвестная операция.")
