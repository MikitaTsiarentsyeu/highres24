print("Введите квадратное уравнение в формате ax^2+bx+c=0:")
equation = input().replace(" ", "")  # убираем пробелы на всякий случай
parts = equation.split("+")

try:
    a = int(parts[0].split("x^2")[0])
    b = int(parts[1].split("x")[0])
    c = int(parts[2].split("=")[0])
except (IndexError, ValueError):
    print("Ошибка ввода. Убедитесь, что уравнение введено правильно!")
    exit()

if a == 0:
    print("Это не квадратное уравнение.")
else:
    D = b**2 - 4*a*c
    if D > 0:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print(f"Уравнение имеет два корня: x₁ = {x1}, x₂ = {x2}.")
    elif D == 0:
        x = -b / (2*a)
        print(f"Уравнение имеет один корень: x = {x}.")
    else:
        print("Уравнение не имеет действительных корней.")
