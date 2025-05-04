def is_prime(n):
    if n < 2:
        return False
    for d in range(2, round(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True

number = int(input("Input number: "))
print("Number is prime? Answer:", is_prime(number))