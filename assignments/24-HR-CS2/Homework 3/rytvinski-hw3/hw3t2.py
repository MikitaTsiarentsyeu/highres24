import math

def parse_quadratic_equation(equation):
    try:
        equation = equation.replace(" ", "").lower().replace("=0", "")
        terms = []
        num = ""
        sign = 1

        for char in equation:
            if char in "+-":
                if num:
                    terms.append(sign * float(num.replace("x*x", "").replace("x", "") or "1"))
                num = ""
                sign = 1 if char == "+" else -1
            else:
                num += char
        
        if num:
            terms.append(sign * float(num.replace("x*x", "").replace("x", "") or "1"))
        
        while len(terms) < 3:
            terms.append(0.0)
        
        return terms
    except:
        print("Invalid equation format. Please enter in the form ax*x+bx+c=0.")
        return None

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two roots: {root1:.2f} and {root2:.2f}"
    elif discriminant == 0:
        root = -b / (2 * a)
        return f"One root: {root:.2f}"
    else:
        return f"No roots"

equation = input("Enter a quadratic equation in the form ax*x+bx+c=0: ")
coefficients = parse_quadratic_equation(equation)
    
if coefficients:
    a, b, c = coefficients
    print(solve_quadratic(a, b, c))