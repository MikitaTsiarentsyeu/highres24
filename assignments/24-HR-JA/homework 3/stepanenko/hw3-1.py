import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
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


