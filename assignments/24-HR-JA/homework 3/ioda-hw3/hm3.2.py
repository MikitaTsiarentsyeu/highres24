inputStr = input("Enter a equation: ")
inputStr = inputStr.replace("x", "")
inputStr = inputStr.replace("\\", "")
inputStr = inputStr.replace("=0", "")
inputStr = inputStr.split("+")
a = int(inputStr[0])
b = int(inputStr[1])
c = int(inputStr[2])

discriminant = b**2 - 4*a*c
if discriminant > 0:
    rootPlus = (-b + (discriminant ** 0.5)) / (2 * a)
    rootMinus = (-b - (discriminant ** 0.5)) / (2 * a)
    print("Answer 1: ", rootPlus, "\nAnswer 2: ", rootMinus)
elif discriminant == 0:
    root = -b / (2 * a)
    print("Answer: ",root)
else:
    print("Error")