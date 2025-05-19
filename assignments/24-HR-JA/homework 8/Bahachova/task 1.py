#%%

import operator

def calculate(tokens):
    def parse_expression(index):
        values = []
        ops = []

        def apply_operator():
            if len(values) < 2 or not ops:
                raise ValueError("Invalid syntax")
            b = values.pop()
            a = values.pop()
            op = ops.pop()
            values.append(operators[op](a, b))

        while index < len(tokens):
            token = tokens[index]
            if token.isdigit() or '.' in token:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid number: {token}")
            elif token in operators:
                while (ops and precedence[ops[-1]] >= precedence[token]):
                    apply_operator()
                ops.append(token)
            elif token == '(':
                res, index = parse_expression(index + 1)
                values.append(res)
            elif token == ')':
                break
            else:
                raise ValueError(f"Unknown token: {token}")
            index += 1

        while ops:
            apply_operator()

        if len(values) != 1:
            raise ValueError("Syntax error in expression")

        return values[0], index

    result, _ = parse_expression(0)
    return result

def tokenize(expr):
    tokens = []
    number = ''
    for char in expr:
        if char.isdigit() or char == '.':
            number += char
        else:
            if number:
                tokens.append(number)
                number = ''
            if char in '+-*/()':
                tokens.append(char)
            elif char.isspace():
                continue
            else:
                raise ValueError(f"Invalid character: {char}")
    if number:
        tokens.append(number)
    return tokens

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2
}

def main():
    print("Simple Calculator (type 'quit' to exit)")
    while True:
        expr = input("Enter expression: ")
        if expr.lower() == 'quit':
            print("Goodbye!")
            break
        try:
            tokens = tokenize(expr)
            result = calculate(tokens)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()