def fibonacci(n):
    if n < 0:
        return 0
    elif n == 1:
        return 1
    
    first_number = 0
    second_number = 1
    for _ in range(2, n + 1):
        first_number = second_number
        second_number = first_number + second_number
    
    return second_number

n = int(input("Введите номер числа Фибоначчи: "))
print(f"Число Фибоначчи под номером {n} — {fibonacci(n)}")