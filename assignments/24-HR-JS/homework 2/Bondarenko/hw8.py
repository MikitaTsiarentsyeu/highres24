while True:
    expression = input("Введите математическое выражение (или 'выход' для завершения): ")
    
    if expression.lower() == "выход":
        print("Программа завершена.")
        break
    
    try:
        expression = expression.replace(" ", "")
        
        allowed_chars = "0123456789+-*/()."
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Недопустимые символы в выражении!")
        
        operators = "+-*/"
        operator = None
        for op in operators:
            if op in expression:
                operator = op
                break
        
        if operator is None:
            raise ValueError("Оператор не найден! Используйте +, -, * или /")
        
        parts = expression.split(operator)
        if len(parts) != 2:
            raise ValueError("Выражение должно содержать ровно один оператор и два числа!")
        
        num1 = float(parts[0])
        num2 = float(parts[1])
        
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Деление на ноль!")
            result = num1 / num2
        
        print("Результат:", result)
    
    except ValueError as e:
        print("Ошибка:", e)
    except ZeroDivisionError as e:
        print("Ошибка:", e)
    except Exception as e:
        print("Произошла ошибка:", e)
    
    print()  