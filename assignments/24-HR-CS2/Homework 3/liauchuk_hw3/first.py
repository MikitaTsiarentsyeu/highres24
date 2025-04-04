from math import sqrt

def solve(a,b,c):
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + sqrt(D)) / (2 * a)
        x2 = (-b - sqrt(D)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")
    elif D == 0:
        x = (-b / (2 * a))
        print(f"x ={x}")
    else:
        print("x !(= {|R}")

solve(int(input("a:")),int(input("b:")),int(input("c:")))
