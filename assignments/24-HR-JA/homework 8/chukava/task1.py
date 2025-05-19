def tokenize(expr):
    tokens = []
    number = ''

    for char in expr:
        if char.isdigit() or char == '.':
            number += char
        elif char in '+-*/()':
            if number:
                tokens.append(number)
                number = ''
            tokens.append(char)
        elif char.isspace():
            if number:
                tokens.append(number)
                number = ''
        else:
            raise ValueError(f"Invalid character: '{char}'")

    if number:
        tokens.append(number)

    return tokens

def to_rpn(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    ops = []

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
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
            if not ops or ops[-1] != '(':
                raise ValueError("Mismatched parentheses")
            ops.pop()
        else:
            raise ValueError(f"Unknown token: {token}")

    while ops:
        if ops[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(ops.pop())

    return output

def eval_rpn(rpn):
    stack = []
    for token in rpn:
        if token.replace('.', '', 1).isdigit():
            stack.append(float(token))
        else:
            try:
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
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)
            except IndexError:
                raise ValueError("Malformed expression")

    if len(stack) != 1:
        raise ValueError("Malformed expression")
    return stack[0]

def calculate(expression):
    tokens = tokenize(expression)
    rpn = to_rpn(tokens)
    result = eval_rpn(rpn)
    return result

def main():
    print("Welcome to the safe Python calculator.")
    print("Supports +, -, *, / and parentheses. Type 'quit' to exit.\n")

    while True:
        expr = input("Enter expression: ")
        if expr.lower() == 'quit':
            print("Goodbye!")
            break
        try:
            result = calculate(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()