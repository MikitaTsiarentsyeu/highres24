import operator

OPERATORS = {
    '+': (1, operator.add),
    '-': (1, operator.sub),
    '*': (2, operator.mul),
    '/': (2, operator.truediv)
}

def tokenize(expression):
    tokens = []
    number = ''
    for char in expression:
        if char.isdigit() or char == '.':
            number += char
        elif char in OPERATORS or char in '()':
            if number:
                tokens.append(float(number))
                number = ''
            tokens.append(char)
        elif char.isspace():
            if number:
                tokens.append(float(number))
                number = ''
        else:
            raise ValueError(f"Invalid character: {char}")
    if number:
        tokens.append(float(number))
    return tokens

def shuntingYard(tokens):
    output = []
    stack = []
    for token in tokens:
        if isinstance(token, float):
            output.append(token)
        elif token in OPERATORS:
            while (stack and stack[-1] in OPERATORS and
                   OPERATORS[token][0] <= OPERATORS[stack[-1]][0]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            if not stack or stack[-1] != '(':
                raise ValueError("Mismatched parentheses")
            stack.pop()
    while stack:
        if stack[-1] in '()':
            raise ValueError("Mismatched parentheses")
        output.append(stack.pop())
    return output

def evaluateRpn(tokens):
    stack = []
    for token in tokens:
        if isinstance(token, float):
            stack.append(token)
        elif token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Insufficient values in expression")
            b = stack.pop()
            a = stack.pop()
            try:
                result = OPERATORS[token][1](a, b)
            except ZeroDivisionError:
                raise ZeroDivisionError("Division by zero is not allowed")
            stack.append(result)
    if len(stack) != 1:
        raise ValueError("The user input has too many values")
    return stack[0]

def main():
    print("Simple Calculator (type 'quit' to exit)")
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == 'quit':
            print("Goodbye!")
            break
        try:
            tokens = tokenize(expression)
            postFix = shuntingYard(tokens)
            result = evaluateRpn(postFix)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == '__main__':
    main()