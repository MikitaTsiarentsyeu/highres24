a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
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