def tokenize(expression):
    tokens = []
    number = ''
    for ch in expression:
        if ch.isdigit() or ch == '.':
            number += ch
        else:
            if number:
                tokens.append(float(number))
                number = ''
            if ch in '+-*/()':
                tokens.append(ch)
            elif ch.isspace():
                continue
            else:
                raise ValueError(f"invalid character: {ch}")
    if number:
        tokens.append(float(number))
    return tokens

def to_rpn(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    ops = []

    for token in tokens:
        if isinstance(token, float):
            output.append(token)
        elif token in '+-*/':
            while ops and ops[-1] != '(' and precedence.get(ops[-1], 0) >= precedence[token]:
                output.append(ops.pop())
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            if not ops:
                raise ValueError("mismatched parentheses")
            ops.pop()
    while ops:
        if ops[-1] == '(':
            raise ValueError("mismatched parentheses")
        output.append(ops.pop())
    return output

def eval_rpn(rpn):
    stack = []
    for token in rpn:
        if isinstance(token, float):
            stack.append(token)
        else:
            if len(stack) < 2:
                raise ValueError("invalid expression")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("division by zero")
                stack.append(a / b)
    if len(stack) != 1:
        raise ValueError("invalid expression")
    return stack[0]

def simple_calculator():
    print("type 'exit' to quit")

    while True:
        expr = input("enter expression ")

        if expr.lower() in ('exit', 'quit'):
            break

        try:
            tokens = tokenize(expr)
            rpn = to_rpn(tokens)
            result = eval_rpn(rpn)
            print("result", result)
        except Exception as e:
            print("error", e)

simple_calculator()
