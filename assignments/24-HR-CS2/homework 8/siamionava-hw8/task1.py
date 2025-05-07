import operator

def calculate(expression):
    try:
        tokens = tokenize(expression)
        result = evaluate(tokens)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except ValueError:
        return "Error: Invalid number format."
    except Exception:
        return "Error: Invalid expression."

def tokenize(expression):
    token = ""
    tokens = []
    for char in expression:
        if char.isdigit() or char == ".":
            token += char
        elif char in "+-*/()":
            if token:
                tokens.append(float(token))
                token = ""
            tokens.append(char)
        elif char.isspace():
            continue
        else:
            raise ValueError("Unexpected character")
    if token:
        tokens.append(float(token))
    return tokens

def evaluate(tokens):
    def parse_expr(tokens):
        stack = []
        op_stack = []
        i = 0

        while i < len(tokens):
            token = tokens[i]

            if isinstance(token, float):
                stack.append(token)
            elif token in "+-*/":
                while op_stack and precedence(op_stack[-1]) >= precedence(token):
                    apply_operator(stack, op_stack.pop())
                op_stack.append(token)
            elif token == "(":
                sub_expr, j = parse_expr(tokens[i + 1:])
                stack.append(sub_expr)
                i += j
            elif token == ")":
                while op_stack:
                    apply_operator(stack, op_stack.pop())
                return stack[0], i + 1

            i += 1

        while op_stack:
            apply_operator(stack, op_stack.pop())

        return stack[0]

    return parse_expr(tokens)

def precedence(op):
    return {"+": 1, "-": 1, "*": 2, "/": 2}.get(op, 0)

def apply_operator(stack, op):
    if len(stack) < 2:
        raise ValueError("Invalid expression format")
    b, a = stack.pop(), stack.pop()
    
    if op == "+":
        stack.append(a + b)
    elif op == "-":
        stack.append(a - b)
    elif op == "*":
        stack.append(a * b)
    elif op == "/":
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        stack.append(a / b)


print("Simple Calculator (type 'exit' to quit)")
while True:
    expr = input("Enter an expression: ")
    if expr.lower() == "exit":
        print("Goodbye!")
        break
    result = calculate(expr)
    print("Result:", result)
