def calculate(tokens):
    def parse_expression(index = 0):
        result, index = parse_term(index)
        while index < len(tokens) and tokens[index] in ('+', '-'):
            op = tokens[index]
            next_value, index = parse_term(index + 1)
            if op == '+':
                result += next_value
            else:
                result -= next_value
        return result, index

    def parse_term(index):
        result, index = parse_factor(index)
        while index < len(tokens) and tokens[index] in ('*', '/'):
            op = tokens[index]
            next_value, index = parse_factor(index + 1)
            if op == '*':
                result *= next_value
            else:
                if next_value == 0:
                    raise ZeroDivisionError("division by zero")
                result /= next_value
        return result, index

    def parse_factor(index):
        token = tokens[index]
        if token == '(':
            value, index = parse_expression(index + 1)
            if tokens[index] != ')':
                raise SyntaxError("missed parentheses")
            return value, index + 1
        else:
            try:
                value = float(token)
                return value, index + 1
            except ValueError:
                raise ValueError(f"invalid number: {token}")

    value, index = parse_expression()
    if index != len(tokens):
        raise SyntaxError("unexpected extra input")
    return value

def tokenizer(expression):
    tokens = []
    number = ''
    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                tokens.append(number)
                number = ''
            if char in '+-*/()':
                tokens.append(char)
            elif char.isspace():
                continue
            else:
                raise ValueError(f"invalid character: {char}")

    if number:
        tokens.append(number)

    return tokens


expr = input("enter expression: ")
try:
    tokens = tokenizer(expr)
    result = calculate(tokens)
    print("result: ", result)

except ZeroDivisionError as zreoDevisionE:
    print("error: ", zreoDevisionE)

except SyntaxError as syntaxE:
    print("error: ", syntaxE)

except ValueError as valueE:
    print("error: ", valueE)

except Exception as e:
    print("unknown error:", e)