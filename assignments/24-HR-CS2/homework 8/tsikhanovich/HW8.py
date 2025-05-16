def calculate(expression):
    try:
        symbols = symbolize(expression)
        result = evaluate(symbols)
        return result
    except ZeroDivisionError:
        return "Error: Division by zero!"
    except Exception as e:
        return f"Error: {str(e)}"

def symbolize(expr):
    symbols = []
    num = ""
    for char in expr:
        if char.isdigit() or char == ".":
            num += char
        elif char in "+-*/()":
            if num:
                symbols.append(num)
                num = ""
            symbols.append(char)
        elif char == " ":
            continue
        else:
            raise ValueError(f"Invalid character: {char}")
    if num:
        symbols.append(num)
    return symbols

def evaluate(symbols):
    def precedence(sign):
        if sign in "+-":
            return 1
        if sign in "*/":
            return 2
        return 0

    def apply_op(a, b, sign):
        a = float(a)
        b = float(b)
        if sign == '+':
            return a + b
        if sign == '-':
            return a - b
        if sign == '*':
            return a * b
        if sign == '/':
            if b == 0:
                raise ZeroDivisionError()
            return a / b

    output = []
    signs = []

    for symbol in symbols:
        if symbol.replace('.', '', 1).isdigit():
            output.append(symbol)
        elif symbol == '(':
            signs.append(symbol)
        elif symbol == ')':
            while signs and signs[-1] != '(':
                b = output.pop()
                a = output.pop()
                sign = signs.pop()
                output.append(apply_op(a, b, sign))
            signs.pop()  # remove '('
        elif symbol in "+-*/":
            while signs and precedence(signs[-1]) >= precedence(symbol):
                b = output.pop()
                a = output.pop()
                sign = signs.pop()
                output.append(apply_op(a, b, sign))
            signs.append(symbol)

    while signs:
        b = output.pop()
        a = output.pop()
        sign = signs.pop()
        output.append(apply_op(a, b, sign))

    return output[0]

print("Simple calculator. Type 'quit' to exit.")
while True:
    user_input = input("Enter an expression: ")
    if user_input.lower() == "quit":
        print("Goodbye!")
        break
    result = calculate(user_input)
    print("Result:", result)
