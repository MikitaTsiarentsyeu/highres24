def calculate(expression):
    def tokenize(expr):
        tokens = []
        num = ''
        for ch in expr:
            if ch.isdigit() or ch == '.':
                num += ch
            else:
                if num:
                    tokens.append(float(num))
                    num = ''
                if ch in '+-*/()':
                    tokens.append(ch)
                elif ch.isspace():
                    continue
                else:
                    raise ValueError(f"Недопустимый символ: {ch}")
        if num:
            tokens.append(float(num))
        return tokens

    def to_rpn(tokens):
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        ops = []

        for token in tokens:
            if isinstance(token, float):
                output.append(token)
            elif token in '+-*/':
                while ops and ops[-1] != '(' and precedence[ops[-1]] >= precedence[token]:
                    output.append(ops.pop())
                ops.append(token)
            elif token == '(':
                ops.append(token)
            elif token == ')':
                while ops and ops[-1] != '(':
                    output.append(ops.pop())
                if not ops:
                    raise ValueError("Несогласованные скобки")
                ops.pop()
        while ops:
            if ops[-1] == '(':
                raise ValueError("Несогласованные скобки")
            output.append(ops.pop())

        return output

    def eval_rpn(rpn):
        stack = []
        for token in rpn:
            if isinstance(token, float):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Недостаточно операндов")
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
                        raise ZeroDivisionError("Деление на ноль")
                    stack.append(a / b)
        if len(stack) != 1:
            raise ValueError("Ошибка вычисления")
        return stack[0]

    tokens = tokenize(expression)
    rpn = to_rpn(tokens)
    result = eval_rpn(rpn)
    return result

def main():
    print("Добро пожаловать в калькулятор. Введите 'выход' для завершения.")
    while True:
        expr = input("Введите выражение: ")
        if expr.lower() in ('выход', 'quit', 'exit'):
            print("До свидания!")
            break
        try:
            result = calculate(expr)
            print("Результат:", result)
        except Exception as e:
            print("Ошибка:", e)

if __name__ == '__main__':
    main()
