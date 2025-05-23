class CalculatorError(Exception):
    pass


def tokenize(expression):
    tokens = []
    current_number = ''
    for char in expression:
        if char.isdigit() or char == '.':
            current_number += char
        elif char in '+-*/()':
            if current_number:
                tokens.append(current_number)
                current_number = ''
            tokens.append(char)
        elif char.isspace():
            if current_number:
                tokens.append(current_number)
                current_number = ''
        else:
            raise CalculatorError(f"Invalid character: '{char}'")
    if current_number:
        tokens.append(current_number)
    return tokens


def parse_expression(tokens):
    position = 0

    def evaluate_binary_operation(left, right, operator):
        if operator == '+':
            return left + right
        elif operator == '-':
            return left - right
        elif operator == '*':
            return left * right
        elif operator == '/':
            if right == 0:
                raise CalculatorError("Division by zero.")
            return left / right
        else:
            raise CalculatorError(f"Unsupported operator: {operator}")

    def parse_add_sub():
        nonlocal position
        result = parse_mul_div()
        while position < len(tokens) and tokens[position] in ('+', '-'):
            operator = tokens[position]
            position += 1
            right = parse_mul_div()
            result = evaluate_binary_operation(result, right, operator)
        return result

    def parse_mul_div():
        nonlocal position
        result = parse_number_or_group()
        while position < len(tokens) and tokens[position] in ('*', '/'):
            operator = tokens[position]
            position += 1
            right = parse_number_or_group()
            result = evaluate_binary_operation(result, right, operator)
        return result

    def parse_number_or_group():
        nonlocal position
        if position >= len(tokens):
            raise CalculatorError("Unexpected end of expression.")
        token = tokens[position]

        if token == '(':
            position += 1
            result = parse_add_sub()
            if position >= len(tokens) or tokens[position] != ')':
                raise CalculatorError("Missing closing parenthesis.")
            position += 1
            return result
        elif token == '-':
            position += 1
            return -parse_number_or_group()
        else:
            position += 1
            try:
                return float(token)
            except ValueError:
                raise CalculatorError(f"Invalid number: {token}")

    result = parse_add_sub()
    if position < len(tokens):
        raise CalculatorError("Unexpected token after expression.")
    return result


def main():
    print("Simple Calculator (type 'quit' to exit)")
    while True:
        try:
            expression = input("Enter expression: ").strip()
            if expression.lower() == 'quit':
                print("Goodbye!")
                break
            tokens = tokenize(expression)
            result = parse_expression(tokens)
            print("Result:", result)
        except CalculatorError as e:
            print("Error:", e)
        except Exception as e:
            print("Unknown error:", e)


if __name__ == "__main__":
    main()
