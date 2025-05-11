def tokenize_expression(expr):
    tokens = []
    current_number = ''
    for character in expr:
        if character.isdigit() or character == '.':
            current_number += character
        elif character in '+-*/()':
            if current_number:
                tokens.append(float(current_number))
                current_number = ''
            tokens.append(character)
        elif character.isspace():
            if current_number:
                tokens.append(float(current_number))
                current_number = ''
        else:
            raise ValueError(f"Недопустимый символ: {character}")
    if current_number:
        tokens.append(float(current_number))
    return tokens

def evaluate_tokens(tokens):
    def evaluate_expression(pos):
        value, pos = evaluate_term(pos)
        while pos < len(tokens) and tokens[pos] in ('+', '-'):
            operator = tokens[pos]
            next_value, pos = evaluate_term(pos + 1)
            value = value + next_value if operator == '+' else value - next_value
        return value, pos

    def evaluate_term(pos):
        value, pos = evaluate_factor(pos)
        while pos < len(tokens) and tokens[pos] in ('*', '/'):
            operator = tokens[pos]
            next_value, pos = evaluate_factor(pos + 1)
            if operator == '*':
                value *= next_value
            else:
                if next_value == 0:
                    raise ZeroDivisionError("Деление на ноль")
                value /= next_value
        return value, pos

    def evaluate_factor(pos):
        token = tokens[pos]
        if token == '(':
            value, pos = evaluate_expression(pos + 1)
            if tokens[pos] != ')':
                raise ValueError("Отсутствует закрывающая скобка")
            return value, pos + 1
        elif isinstance(token, float):
            return token, pos + 1
        elif token == '-':
            value, pos = evaluate_factor(pos + 1)
            return -value, pos
        else:
            raise ValueError(f"Неожиданный токен: {token}")

    return evaluate_expression(0)

def run_calculator():
    print("Простой калькулятор. Введите 'q' для выхода.")
    while True:
        user_input = input("Введите выражение: ")
        if user_input.lower() == 'q':
            break
        try:
            tokens = tokenize_expression(user_input)
            result, pos = evaluate_tokens(tokens)
            if pos != len(tokens):
                raise ValueError("Некорректный синтаксис")
            print("Результат:", result)
        except Exception as error:
            print("Ошибка:", error)

run_calculator()