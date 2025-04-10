def calculate_quadratic_equation(a: float, b: float, c: float):
    D = b ** 2 - 4 * a * c
    
    if D < 0:
        return "D < 0, no roots"
    elif D == 0:
        x1 = (-b + D ** 0.5) / 2 * a
        return f"One root X = {x1}"
    else:
        x1 = (-b + D ** 0.5) / 2 * a
        x2 = (-b - D ** 0.5) / 2 * a
        
        return f"Two roots X1 = {x1}\nX2 = {x2}"
        
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

print(calculate_quadratic_equation(a, b, c))
    
    
    
    
    