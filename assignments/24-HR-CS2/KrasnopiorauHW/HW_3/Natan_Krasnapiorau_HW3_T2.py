import re
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
    
def ExtractCoefficients(equation):

    equation = equation.replace(" ", "").split("=")[0]
    
    matches = re.findall(r"([+-]?\d*)(x\^2|x)?", equation)

    for match in matches:
        coeff, term = match
        if term == "x^2":
            a = int(coeff) 
        elif term == "x":
            b = int(coeff) 
        elif coeff:
            c = int(coeff)

    return SolveQuadraticEquation(a, b, c)

#For a correct work of the code enter the quadratic equation in format like this: "2x^2 + 3x + 1 = 0" or "1x^2 + 1x + 1 = 0"
    
print(ExtractCoefficients("-1x^2 - 1x + 2 = 0"))