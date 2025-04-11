import math

def isNumber(something):
    try:
        float(something)
        return True
    except ValueError:
        return False

while True:
    equation = input("Please enter the equations in the form ax * x + b * x + c = 0: ")
    equation = equation.replace(" ", "").replace("x", "").replace("*", "")
    if isNumber(equation.split("+")[0]):
        a = float(equation.split("+")[0])
        if isNumber(equation.split("+")[1]):
            b = float(equation.split("+")[1])
            if isNumber(equation.split("+")[2].split("=")[0]):
                c = float(equation.split("+")[2].split("=")[0])
                break
            else:
                print("The expression has been entered incorrectly")
        else:
            print("The expression has been entered incorrectly")
    else:
        print("The expression has been entered incorrectly")

d = (b ** 2) - (4 * a * c)

if d == 0:
  x = -b / (2 * a)
  print(f"x = {x}")
elif d > 0:
  x1 = ((-b + math.sqrt(d)) / (2 * a))
  x2 = ((-b - math.sqrt(d)) / (2 * a))
  print(f"x1 = {x1} \nx2 = {x2}")
else:
  print("Discriminant < 0, so there are no roots.")