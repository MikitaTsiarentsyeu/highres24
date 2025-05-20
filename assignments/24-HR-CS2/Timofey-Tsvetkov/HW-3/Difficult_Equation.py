import math
print("Input Equation")
EQ = str(input())

a = int(EQ[0:2])

b = int(EQ[3:5])

c = int(EQ[6:8])

dis = math.sqrt(b **2 - 4 * a * c)

if dis == 0:
    print("the only solution is " (-b) / 2 * a)
else:
    first_sol = (-b - dis) / 2 * a
    second_sol = (-b + dis) / 2 * a
    print("there is only 2 solutions here", first_sol, "and", second_sol)





