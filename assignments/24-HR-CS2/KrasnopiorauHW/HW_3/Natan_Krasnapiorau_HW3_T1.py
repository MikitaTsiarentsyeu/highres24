import math

def SolveQuadraticEquation(a, b, c):

    if a == 0 or b == 0 or c ==0:

        return "Invalid parameters"
    
    discriminant = math.pow(b, 2) - (4 * a * c)

    if discriminant < 0:
        return "Equation does not have roots"
    elif discriminant == 0:
        return f"The only root of equation is {- (b / (2 * a))}"
    elif discriminant > 0:
        return f"The roots of equation are {((- b) + math.sqrt(discriminant)) / (2 * a)} and {((- b) - math.sqrt(discriminant)) / (2 * a)}"
    
print(SolveQuadraticEquation(2, 4, 2))