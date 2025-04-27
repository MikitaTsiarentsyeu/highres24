def tokenize(expression):
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
        elif char == ' ':
            if number:
                tokens.append(float(number))
                number = ''
        else:
            raise ValueError(f"Invalid character found: '{char}'")
    if number:
        tokens.append(float(number))
    return tokens


def parse(tokens):
    def parse_expression(index):
        values = []
        operators = []

        def apply_operator():
            right = values.pop()
            left = values.pop()
            op = operators.pop()
            if op == '+':
                values.append(left + right)
            elif op == '-':
                values.append(left - right)
            elif op == '*':
                values.append(left * right)
            elif op == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                values.append(left / right)

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        while index < len(tokens):
            token = tokens[index]

            if isinstance(token, float):
                values.append(token)
            elif token in '+-*/':
                while (operators and
                       precedence[operators[-1]] >= precedence[token]):
                    apply_operator()
                operators.append(token)
            elif token == '(':
                result, index = parse_expression(index + 1)
                values.append(result)
            elif token == ')':
                break
            index += 1

        while operators:
            apply_operator()

        return values[0], index

    result, _ = parse_expression(0)
    return result


def calculator():
    print("Type quit to exit")
    while True:
        expression = input("Enter expression: ").strip()
        if expression.lower() == 'quit':
            break
        try:
            tokens = tokenize(expression)
            result = parse(tokens)
            print(f"Result: {result}")
        except ZeroDivisionError as zde:
            print(f"Error: {zde}")
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected Error: {e}")


calculator()
