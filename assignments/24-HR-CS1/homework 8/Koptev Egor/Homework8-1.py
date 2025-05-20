def Calculator():
    print("Supported operations: +, -, *, /, and parentheses for grouping.")
    print("Enter 'quit' to exit.\n")

    while True:
        inputs = input("Enter a mathematical expression: ")
        expression = inputs.strip()

        if expression.lower() == 'quit':
            break

        if not expression:
            print("Error: Empty expression. Please try again.")
            continue

        try:
            result = evaluate_expression(expression)
            print(f"Result: {result}\n")
        except (ValueError, ZeroDivisionError, IndexError) as e:
            print(f"Error: {str(e)}. Please try again.\n")


def evaluate_expression(expr):
    expr = expr.replace(" ", "")
    allowed_chars = set("0123456789+-*/().")

    if not all(c in allowed_chars for c in expr):
        raise ValueError("Invalid characters in expression")

    if not are_balanced(expr):
        raise ValueError("Unbalanced parentheses in expression")

    array = break_to_array(expr)

    return evaluate_array(array)


def are_balanced(expr): #Numbers of ) equal (?
    balance = 0
    for char in expr:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0

def break_to_array(expr):
    array = []
    i = 0
    while i < len(expr):
        if expr[i] in '+-*/()': #Is symbol operator?
            array.append(expr[i])
            i += 1
        elif expr[i].isdigit() or expr[i] == '.':
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'): #Is next symbol part of number too?
                j += 1
            array.append(expr[i:j])
            i = j
        else:
            raise ValueError(f"Unexpected character: {expr[i]}")
    return array


def evaluate_array(array):
    output = []
    operators = []
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    for token in array: #From infix expression to postfix
        if token.replace('.', '').isdigit():
            output.append(float(token))
        elif token in '+-*/':
            while (operators and operators[-1] != '(' and
                   precedence[operators[-1]] >= precedence[token]):
                output.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                output.append(operators.pop())
            if not operators:
                raise ValueError("Mismatched parentheses")
            operators.pop()  # Remove the '('

    while operators:
        if operators[-1] == '(':
            raise ValueError("Mismatched parentheses")
        output.append(operators.pop())

    memory = []
    for token in output: #Postfix expression evaluation
        if isinstance(token, float): #If float, transfer to memory
            memory.append(token)
        else:
            if len(memory) < 2:
                raise ValueError("Invalid expression")
            b = memory.pop()
            a = memory.pop()
            if token == '+':
                memory.append(a + b)
            elif token == '-':
                memory.append(a - b)
            elif token == '*':
                memory.append(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Division by zero")
                memory.append(a / b)

    if len(memory) != 1:
        raise ValueError("Invalid expression")

    return memory[0]


Calculator()