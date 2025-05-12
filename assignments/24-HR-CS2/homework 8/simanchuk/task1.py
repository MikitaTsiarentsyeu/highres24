def get_tokens(expression):
    tokens = []
    number = ''
    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        elif char in '+-*/()':
            if number:
                tokens.append(float(number))
                number = ''
            tokens.append(char)
        elif char.isspace():
            if number:
                tokens.append(float(number))
                number = ''
        else:
            raise ValueError(f"Invalid: {char}")
    if number:
        tokens.append(float(number))
    return tokens

def parse(tokens):
    def parse_expression(index):
        value, index = parse_term(index)
        while index < len(tokens) and tokens[index] in ('+', '-'):
            op = tokens[index]
            next_value, index = parse_term(index + 1)
            if op == '+':
                value += next_value
            else:
                value -= next_value
        return value, index

    def parse_term(index):
        value, index = parse_factor(index)
        while index < len(tokens) and tokens[index] in ('*', '/'):
            op = tokens[index]
            next_value, index = parse_factor(index + 1)
            if op == '*':
                value *= next_value
            else:
                if next_value == 0:
                    raise ZeroDivisionError("Division by zero")
                value /= next_value
        return value, index

    def parse_factor(index):
        token = tokens[index]
        if token == '(':
            value, index = parse_expression(index + 1)
            if tokens[index] != ')':
                raise ValueError("Expected closing parenthesis")
            return value, index + 1
        elif isinstance(token, float):
            return token, index + 1
        elif token == '-':
            value, index = parse_factor(index + 1)
            return -value, index
        else:
            raise ValueError(f"Unexpected token: {token}")

    return parse_expression(0)

def calculator():
    print("Simple Calculator. Type 'q' to quit.")
    while True:
        expr = input("Enter expression: ")
        if expr.lower() == 'q':
            break
        try:
            tokens = get_tokens(expr)
            result, index = parse(tokens)
            if index != len(tokens):
                raise ValueError("Invalid syntax")
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

calculator()
