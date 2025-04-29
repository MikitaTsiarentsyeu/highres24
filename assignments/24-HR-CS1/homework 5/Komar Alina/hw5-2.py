def is_prime(numb: int) -> bool:
    if numb <= 1:
        return False
    if numb == 2:
        return True
    max_prime = numb // 2 + 1
    for i in range(2, max_prime):
        if numb % i == 0:
            return False
    return True

num = int(input("Enter a number for finding if prime: "))
print(is_prime(num))
