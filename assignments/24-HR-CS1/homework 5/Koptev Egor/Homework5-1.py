def fibonacci(n: int) -> int:
    if n <= 0:
        print("Please enter a positive integer")
        return -1 #Error code
    elif n == 1:
        return 0
    elif n == 2:
        return 1

    a = 0 #First num in Fibonacci seq
    b = 1 #Second num in Fibonacci seq
    calculation = n - 2 #Nums of calculation. Min possible calculation is 1, but input is 3
    for i in range(calculation):
        a, b = b, a + b
    return b

num = int(input("Enter a number: "))
print(fibonacci(num))