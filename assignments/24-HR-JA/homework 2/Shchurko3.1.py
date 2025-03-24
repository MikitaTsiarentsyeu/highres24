import math

a=float(input("Enter coef a: "))
b=float(input("Enter coef b: "))
c=float(input("Enter coef c: "))
D=b*b-4*a*c
if D<0:
    print("No solution for this coefs")
elif D==0:
    print('one solution:', ((-b)+math.sqrt(D))/(2*a))
else:
    print('two solutions:', ((-b)+math.sqrt(D))/(2*a), ((-b)-math.sqrt(D))/(2*a))