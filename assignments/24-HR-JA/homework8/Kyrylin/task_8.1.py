def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def times(a, b):
    return a * b

def div(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed")
    return a / b

def split_tokens(expr):
    tokens = []
    number_buffer = ''
    idx = 0
    while idx < len(expr):
        ch = expr[idx]
        if ch.isdigit() or ch == '.':
            number_buffer += ch
        else:
            if number_buffer:
                tokens.append(float(number_buffer))
                number_buffer = ''
            if ch in '+-*/()':
                tokens.append(ch)
            elif ch == ' ':
                pass
            else:
                raise ValueError(f"Invalid character: '{ch}'")
        idx += 1
    if number_buffer:
        tokens.append(float(number_buffer))
    return tokens

def parse_factor(tokens):
    if not tokens:
        raise ValueError("Unexpected end of expression")
    token = tokens.pop(0)
    if isinstance(token, float):
        return token
    elif token == '(':
        val = parse_expression(tokens)
        if not tokens or tokens.pop(0) != ')':
            raise ValueError("Missing closing parenthesis")
        return val
    elif token == '-':
        return minus(0, parse_factor(tokens))
    else:
        raise ValueError(f"Unexpected token: {token}")

def parse_term(tokens):
    val = parse_factor(tokens)
    while tokens and tokens[0] in ('*', '/'):
        op = tokens.pop(0)
        next_val = parse_factor(tokens)
        if op == '*':
            val = times(val, next_val)
        else:
            val = div(val, next_val)
    return val

def parse_expression(tokens):
    val = parse_term(tokens)
    while tokens and tokens[0] in ('+', '-'):
        op = tokens.pop(0)
        next_val = parse_term(tokens)
        if op == '+':
            val = plus(val, next_val)
        else:
            val = minus(val, next_val)
    return val

def evaluate(expr):
    expr = expr.replace(' ', '')
    tokens = split_tokens(expr)
    result = parse_expression(tokens)
    if tokens:
        raise ValueError("Invalid expression: extra tokens")
    return result

def calculator():
    print("Type 'exit' to quit")
    while True:
        user_input = input("Enter an expression: ")
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            answer = evaluate(user_input)
            print("Result:", answer)
        except ZeroDivisionError as zde:
            print("Error:", zde)
        except ValueError as ve:
            print("Error:", ve)
        except Exception as e:
            print("Unexpected error:", e)

if __name__ == "__main__":
    calculator()
