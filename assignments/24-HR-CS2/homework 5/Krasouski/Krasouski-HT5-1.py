def fibonachiFounder(n:int) -> int:
    if n < 0:
        return -1

    i = 2
    previousNum1 = 1
    previousNum2 = 1
    while i <= n:
        result = previousNum1 + previousNum2
        i += 1

        previousNum2 = previousNum1
        previousNum1 = result

    return previousNum1

userInput = int(input("print Fibonachi num you want to find \n"))
print("Your num is " + str(fibonachiFounder(userInput)))