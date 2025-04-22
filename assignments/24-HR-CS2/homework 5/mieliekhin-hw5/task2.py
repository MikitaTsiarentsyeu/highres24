def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Введите число: "))
if is_prime(n):
    print(f"{n} — простое число.")
else:
    print(f"{n} — не простое число.")