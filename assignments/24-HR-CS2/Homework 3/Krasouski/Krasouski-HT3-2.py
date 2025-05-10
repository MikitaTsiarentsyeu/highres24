import math

print("Welcome to quadratic ecvasion solver")
print("Write equasion in form - ax^2 + bx + c = 0")

userInput = input()

userInput = userInput.replace(" ", "").lower()
firstFormatedInput = userInput.split("=0")[0]
secondFormatedInput = firstFormatedInput.split("x^2")[1]

a = int(firstFormatedInput.split("x^2")[0] or 1)
b = int(secondFormatedInput.split("x")[0] or 1)
c = int(secondFormatedInput.split("x")[1] or 0)

D = (b ** 2) - 4 * a * c

if (D > 0):
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

    print(f"x1: {x1}")
    print(f"x2: {x2}")
elif(D == 0):
    x = -b / (2 * a)
    print(f"x: {x}")
else:
    print("no real roots")