import math

def main():
    try:
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))

        d = b**2 - 4*a*c

        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print(f"Two real roots: x1 = {x1}, x2 = {x2}")
        elif d == 0:
            x = -b / (2*a)
            print(f"One real root: x = {x}")
        else:
            print("No real roots")

    except ValueError:
        print("Invalid input")

if __name__ == "__main__":
    main()