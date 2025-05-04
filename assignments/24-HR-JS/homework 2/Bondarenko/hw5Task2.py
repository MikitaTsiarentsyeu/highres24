def is_prime(numb: int) -> bool:
    if numb < 2:
        return False
    
    for i in range(2, int(numb ** 0.5) + 1):
        if numb % i == 0:
            return False  
    return True  

number = int(input("Введите число для проверки: "))
if is_prime(number):
    print(f"{number} - простое число")
else:
    print(f"{number} - не простое число")