def calc(a, b, sign):
    if sign == "+":
        return a + b
    elif sign == "-":
        return a - b
    elif sign == "*":
        return a * b
    elif sign == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b
    else:
        raise ValueError("Unknown operator")


def priority(opr):
    return {"+": 1, "-": 1, "*": 2, "/": 2}.get(opr, 0)


def tokenize(expr):
    tokens = []
    num = ''
    for char in expr:
        if char.isdigit() or char == '.':
            num += char
        elif char in '+-*/()':
            if num:
                tokens.append(num)
                num = ''
            tokens.append(char)
        elif char == ' ':
            continue
        else:
            raise ValueError(f"Invalid character: {char}")
    if num:
        tokens.append(num)
    return tokens


def evaluate(expression):
    tokens = tokenize(expression)
    values, ops = [], []

    def compute():
        b, a = values.pop(), values.pop()
        values.append(calc(a, b, ops.pop()))

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            values.append(float(token))
        elif token == "(":
            ops.append(token)
        elif token == ")":
            while ops and ops[-1] != "(":
                compute()
            if not ops:
                raise ValueError("Missed parentheses")
            ops.pop()
        elif token in "+-*/":
            while ops and ops[-1] != "(" and priority(ops[-1]) >= priority(token):
                compute()
            ops.append(token)
        else:
            raise ValueError(f"Invalid token: {token}")

    while ops:
        if ops[-1] == "(":
            raise ValueError("Missed parentheses")
        compute()

    if len(values) != 1:
        raise ValueError("Invalid expression")
    return values[0]


print("Type 'quit' to exit.")
while True:
    expr = input("Enter an expression: ")
    if expr.lower() == "quit":
        break
    try:
        print("Result:", evaluate(expr))
    except Exception as e:
        print("Error:", e)
