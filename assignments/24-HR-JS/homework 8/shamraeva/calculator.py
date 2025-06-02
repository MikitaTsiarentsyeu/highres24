def calculate(expression):
    try:
        tokens = tokenize(expression)
        result = evaluate(tokens)
        return result
    except RuntimeError as e:
        raise RuntimeError(f"Error: {e}")


def tokenize(expr):
    tokens = []
    num = ''
    for char in expr.replace(' ', ''):
        if char.isdigit() or char == '.':
            num += char
        elif char in '+-*/':
            if not num:
                raise RuntimeError("operator without number")
            tokens.append(num)
            tokens.append(char)
            num = ''
        else:
            raise RuntimeError(f"invalid character: {char}")
    if num:
        tokens.append(num)
    return tokens


def evaluate(tokens):
    if not tokens:
        raise RuntimeError("empty expression")

    try:
        result = float(tokens[0])
    except:
        raise RuntimeError(f"invalid number: {tokens[0]}")

    i = 1
    while i < len(tokens) - 1:
        op = tokens[i]
        try:
            num = float(tokens[i + 1])
        except:
            raise RuntimeError(f"invalid number: {tokens[i + 1]}")

        if op == '+':
            result += num
        elif op == '-':
            result -= num
        elif op == '*':
            result *= num
        elif op == '/':
            if num == 0:
                raise RuntimeError("division by zero")
            result /= num
        else:
            raise RuntimeError(f"invalid operator: {op}")
        i += 2

    return result


if __name__ == "__main__":
    print("Welcome")

    while True:
        user_input = input("Enter expression (or 'quit' to exit): ")

        if user_input.strip().lower() == 'quit':
            print("Goodbye!")
            break

        try:
            result = calculate(user_input)
            print(f"Result: {result}")
        except RuntimeError as e:
            print(e)
