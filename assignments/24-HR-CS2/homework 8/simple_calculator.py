def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

def parse_expression(expression):
    try:
        tokens = tokenize(expression)
        result = evaluate(tokens)
        return result
    except ZeroDivisionError as e:
        raise e
    except Exception as e:
        raise ValueError("Invalid expression. Please check your input.") from e

def tokenize(expression):
    tokens = []
    num = ''
    for char in expression:
        if char.isdigit() or char == '.':
            num += char
        else:
            if num:
                tokens.append(float(num))
                num = ''
            if char in '+-*/()':
                tokens.append(char)
    if num:
        tokens.append(float(num))
    return tokens

def evaluate(tokens):
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operator(operators, values):
        operator = operators.pop()
        b = values.pop()
        a = values.pop()
        if operator == '+':
            values.append(add(a, b))
        elif operator == '-':
            values.append(subtract(a, b))
        elif operator == '*':
            values.append(multiply(a, b))
        elif operator == '/':
            values.append(divide(a, b))

    operators = []
    values = []
    i = 0
    while i < len(tokens):
        token = tokens[i]
        if isinstance(token, float):
            values.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop() 
        elif token in '+-*/':
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(token)):
                apply_operator(operators, values)
            operators.append(token)
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]

def main():
    expression = input("Enter expression: ").strip()
    try:
        result = parse_expression(expression)
        print(f"Result: {result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

main()