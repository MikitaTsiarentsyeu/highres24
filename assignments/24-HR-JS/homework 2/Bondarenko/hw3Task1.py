import math


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def get_coefficient(name):
    while True:
        value = input(f"Пожалуйста, введите значение для {name}: ")
        if is_number(value):
            return float(value)
        else:
            print("Вы можете ввести только число. Попробуйте еще раз")


print("Давайте решим квадратное уравнение вида ax² + bx + c = 0!")
a = get_coefficient("a")
b = get_coefficient("b")
c = get_coefficient("c")


print(f"Вы ввели: a = {a}, b = {b}, c = {c}")


if a == 0:
    print("Извините, 'a' не может быть нулём. Это не квадратное уравнение.")
else:
   
    discriminant = b**2 - 4*a*c
    print(f"Дискриминант равен: {discriminant}")

    
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        print(f"Есть два действительных корня: x1 = {x1}, x2 = {x2}")
    elif discriminant == 0:
        x = -b / (2*a)
        print(f"Есть один действительный корень: x = {x}")
    else:
        real_part = -b / (2*a)
        imaginary_part = math.sqrt(-discriminant) / (2*a)
        print(f"Корни сложные: {real_part} + {imaginary_part}i и {real_part} - {imaginary_part}i")
    