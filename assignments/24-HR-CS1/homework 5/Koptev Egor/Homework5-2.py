def isPrime(numb: int) -> bool:
    if numb <= 1:  #Number <= 1 -> not prime
        return False
    for i in range(2, numb):  #Range from 2 to our number (exclusive)
        if numb % i == 0:  #If our number divide to range number without remainder -> not prime
            return False
    return True  #If not -> prime

num = int(input("Enter a number: "))
print(isPrime(num))