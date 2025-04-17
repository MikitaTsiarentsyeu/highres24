import math


def solve_quadratic_simple():
    while True:
        try:
            equation = input("Введите квадратное уравнение (например, 2x*x-5x+3=0): ").replace(" ", "")

            if not equation.endswith("=0"):
                raise ValueError("Уравнение должно быть вида ax²+bx+c=0")

            parts = equation[:-2].replace("-", "+-").split("+")
            if "" in parts:
                parts.remove("")

            a, b, c = 0.0, 0.0, 0.0

            for part in parts:
                if "x*x" in part:
                    a_str = part.replace("x*x", "")
                    a = float(a_str) if a_str not in ["", "+"] else 1.0
                    a = float(a_str) if a_str not in ["", "+"] else (-1.0 if "-" in part else 1.0)
                elif "x" in part:
                    b_str = part.replace("x", "")
                    b = float(b_str) if b_str not in ["", "+"] else 1.0
                    b = float(b_str) if b_str not in ["", "+"] else (-1.0 if "-" in part else 1.0)
                else:
                    c = float(part)

            if a == 0:
                raise ValueError("Коэффициент 'a' не может быть 0 (это не квадратное уравнение)")

            D = b * b - 4 * a * c
            if D < 0:
                print("No solution for this coefs")
            elif D == 0:
                print('one solution:', ((-b) + math.sqrt(D)) / (2 * a))
            else:
                print('two solutions:', ((-b) + math.sqrt(D)) / (2 * a), ((-b) - math.sqrt(D)) / (2 * a))

            break

        except ValueError as e:
            print(f"Ошибка: {e}. Попробуйте снова.")


solve_quadratic_simple()
