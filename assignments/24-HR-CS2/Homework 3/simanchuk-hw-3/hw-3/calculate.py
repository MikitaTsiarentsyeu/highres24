from decimal import Decimal as D


def solvEquation(a, b , c):
    disc = b**2 - D(4)*a * c

    if disc > 0:
        x1 = (-b - disc.sqrt()) / (D(2) * a)
        x2 = (-b + disc.sqrt()) / (D(2) * a)
        return x1,x2
    elif disc == 0:
        return -b / (2 * a) 
    else:
        return "no roots :)"