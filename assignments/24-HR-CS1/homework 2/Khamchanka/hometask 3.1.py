import math
print ("Write a ")
a = int(input()) 
if a == 0:
    print("Exception")
else:
     print ("Write b")
     b = int(input())
     print ("Write c ")
     c = int(input())
     discriminant = b ** 2 - 4 * a * c
     if discriminant > 0 :
          x1 = (-b - math.sqrt(discriminant)) / (2 * a)
          x2 = (-b + math.sqrt(discriminant)) / (2 * a)
          print(x1,x2)
     elif discriminant == 0 : 
          x = -b / (2 * a)
          print(x)
     else :
          print ("No x1 & x2")