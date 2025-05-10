def calculate():
    while True:
        try:
            expression = input("Enter an expression (q to quit): ").strip()
            if expression.lower() == 'q':
                print("Goodbye!")
                break
            result = parse_expression(expression)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {str(e)}")

def parse_expression(expr):
    tokens = tokensize(expr)
    return evaluate(tokens)

def tokensize(expr):
    tokens = []
    i = 0
    while i < len(expr):
        c = expr[i]
        if c.isspace():
            i += 1
            continue
        if c in '()+-*/':
            tokens.append(c)
            i += 1
        elif c.isdigit() or c == '.':
            num = []
            decimal_count = 0
            while i < len(expr) and (expr[i].isdigit() or expr[i] == '.'):
                if expr[i] == '.':
                    decimal_count += 1
                    if decimal_count > 1:
                        raise ValueError("Multiple decimals in number")
                num.append(expr[i])
                i += 1
            tokens.append(float(''.join(num)))
        else:
            raise ValueError(f"Invalid character: {c}")
    return tokens

def evaluate(tokens):
    try:
        value, _ = evaluate_expression(tokens, 0)
        return value
    except IndexError:
        raise ValueError("Unexpected end of expression")
    
def evaluate_expression(tokens, index):
    value, index = evaluate_term(tokens, index)
    while index < len(tokens):
        token = tokens[index]
        if token == '+':
            next_value, index = evaluate_term(tokens, index + 1)
            value += next_value
        elif token == '-':
            next_value, index = evaluate_term(tokens, index + 1)
            value -= next_value
        else:
            break
    return value, index

def evaluate_term(tokens, index):
    value, index = evaluate_factor(tokens, index)
    while index < len(tokens):
        token = tokens[index]
        if token == '*':
            next_value, index = evaluate_factor(tokens, index + 1)
            value *= next_value
        elif token == '/':
            next_value, index = evaluate_factor(tokens, index + 1)
            if next_value == 0:
                raise ZeroDivisionError("Division by zero")
            value /= next_value
        else:
            break
    return value, index

def evaluate_factor(tokens, index):
    token = tokens[index]
    if isinstance(token, float):
        return token, index + 1
    if token == '(':
        value, index == evaluate_expression(tokens, index + 1)
        if index >= len(tokens) or tokens[index] != ')':
            raise ValueError("Mismatched parentheses")
        return value, index + 1
    if token == '-':
        value, index = evaluate_factor(tokens, index + 1)
        return -value, index
    raise ValueError("Unexpected token: " + str(token))

if __name__ == "__main__":
    calculate()