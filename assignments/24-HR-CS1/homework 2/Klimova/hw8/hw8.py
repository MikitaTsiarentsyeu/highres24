def tokenize(expr: str):
    tokens = []
    num = ''
    for ch in expr:
        if ch.isdigit() or ch == '.':
            num += ch
        elif ch in '+-*/()':
            if num:
                tokens.append(float(num))
                num = ''
            tokens.append(ch)
        elif ch.isspace():
            continue
        else:
            raise ValueError(f"Invalid character: {ch}")
    if num:
        tokens.append(float(num))
    return tokens

def shunting_yard(tokens):
    output = []
    ops = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    
    for token in tokens:
        if isinstance(token, float):
            output.append(token)
        elif token in precedence:
            while (ops and ops[-1] != '(' and
                   precedence.get(ops[-1], 0) >= precedence[token]):
                output.append(ops.pop())
            ops.append(token)
        elif token == '(':
            ops.append(token)
        elif token == ')':
            while ops and ops[-1] != '(':
                output.append(ops.pop())
            if not ops or ops[-1] != '(':
                raise ValueError("Mismatched parentheses")
            ops.pop()
        else:
            raise ValueError(f"Unknown token: {token}")
    
    while ops:
        if ops[-1] in '()':
            raise ValueError("Mismatched parentheses")
        output.append(ops.pop())
    
    return output

def evaluate_rpn(rpn):
    stack = []
    for token in rpn:
        if isinstance(token, float):
            stack.append(token)
        else:
            if len(stack) < 2:
                raise ValueError("Insufficient values in expression")
            b = stack.pop()
            a = stack.pop()
            if token == '+': stack.append(a + b)
            elif token == '-': stack.append(a - b)
            elif token == '*': stack.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(a / b)
            else:
                raise ValueError(f"Invalid operator: {token}")
    if len(stack) != 1:
        raise ValueError("Invalid expression")
    return stack[0]

def calculate(expression: str):
    tokens = tokenize(expression)
    rpn = shunting_yard(tokens)
    return evaluate_rpn(rpn)

print("Simple Calculator. Type 'quit' to exit.")
while True:
    expr = input("Enter expression: ")
    if expr.lower() in ('quit', 'exit'):
        print("Goodbye!")
        break
    try:
        result = calculate(expr)
        print("Result:", result)
    except Exception as e:
        print("Error:", e)
