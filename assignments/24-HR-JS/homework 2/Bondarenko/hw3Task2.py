import math
import re


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


while True:
    print("Давайте решим квадратное уравнение! Введите его в виде ax²+bx+c=0 (например, 2x²+3x-5=0).")
    equation = input("Ваше уравнение: ")
    
    
    equation = equation.replace(" ", "").replace("x*x", "x²")
    if not equation.endswith("=0"):
        print("Упс! Уравнение должно заканчиваться на '=0'. Попробуйте ещё раз!")
        continue
    
    
    equation = equation[:-2]
    
    
    terms = re.split(r'(?=[+-])', equation)
    if terms[0] and terms[0][0] not in ['+', '-']:
        terms[0] = '+' + terms[0]  
    
     
    a = b = c = 0
    valid = True
    
    
    for term in terms:
        term = term.strip()
        if 'x²' in term:
            coeff = term.replace('x²', '')
            if coeff in ['+', '-', '']:
                a = 1 if coeff in ['+', ''] else -1
            else:
                if not is_number(coeff):
                    valid = False
                    break
                a = float(coeff)
        elif 'x' in term and 'x²' not in term:
            coeff = term.replace('x', '')
            if coeff in ['+', '-', '']:
                b = 1 if coeff in ['+', ''] else -1
            else:
                if not is_number(coeff):
                    valid = False
                    break
                b = float(coeff)
        else:
            if not is_number(term):
                valid = False
                break
            c = float(term) if term else 0
    
    if valid and a != 0:
        break
    else:
        if a == 0:
            print("Упс! 'a' не может быть равен нулю. Это не квадратное уравнение. Попробуйте ещё раз!")
        else:
            print("Формат уравнения неверный. Убедитесь, что оно имеет вид ax²+bx+c=0. Попробуйте ещё раз!")


print(f"Принято! Коэффициенты: a = {a}, b = {b}, c = {c}")


discriminant = b**2 - 4*a*c
print(f"Дискриминант: {discriminant}")

if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2*a)
    x2 = (-b - math.sqrt(discriminant)) / (2*a)
    print(f"Два действительных корня: x1 = {x1}, x2 = {x2}")
elif discriminant == 0:
    x = -b / (2*a)
    print(f"Один действительный корень: x = {x}")
else:
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-discriminant) / (2*a)
    print(f"Корни комплексные: {real_part} + {imaginary_part}i и {real_part} - {imaginary_part}i")
