import re

class CalcEx(Exception):
    pass


class Calculator:
    def __init__(self):
        self.ops_priority = {'+': 1, '-': 1, '*': 2, '/': 2}

    def tokenize(self, expr):
        tokens = re.findall(r'\d+\.?\d*|[()+\-*/]', expr)
        for token in tokens:
            if not re.fullmatch(r'\d+\.?\d*|[()+\-*/]', token):
                raise CalcEx(f"Недопустимый токен: {token}")
        return tokens

    def to_rpn(self, tokens):
        output = []
        stack = []

        for token in tokens:
            if re.fullmatch(r'\d+\.?\d*', token):
                output.append(token)
            elif token in self.ops_priority:
                while (stack and stack[-1] != '(' and
                       self.ops_priority.get(stack[-1], 0) >= self.ops_priority[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack:
                    raise CalcEx("Несоответствие скобок")
                stack.pop()

        while stack:
            if stack[-1] in '()':
                raise CalcEx("Несоответствие скобок")
            output.append(stack.pop())

        return output

    def eval_rpn(self, rpn):
        stack = []

        for token in rpn:
            if re.fullmatch(r'\d+\.?\d*', token):
                stack.append(float(token))
            elif token in '+-*/':
                if len(stack) < 2:
                    raise CalcEx("Недостаточно операндов")
                b, a = stack.pop(), stack.pop()
                match token:
                    case '+': stack.append(a + b)
                    case '-': stack.append(a - b)
                    case '*': stack.append(a * b)
                    case '/':
                        if b == 0:
                            raise CalcEx("Деление на ноль")
                        stack.append(a / b)
            else:
                raise CalcEx(f"Неизвестный элемент в RPN: {token}")

        if len(stack) != 1:
            raise CalcEx("Слишком много значений в стеке")
        return stack[0]

    def calculate(self, expression):
        tokens = self.tokenize(expression)
        rpn = self.to_rpn(tokens)
        return self.eval_rpn(rpn)


def main():
    calc = Calculator()
    print("Для выхода введите 'q'")
    while True:
        expr = input("Введите выражение: ").strip()
        if expr.lower() == 'q':
            print("До свидания!")
            break
        try:
            result = calc.calculate(expr)
            print(f"Результат: {result}")
        except CalcEx as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неизвестная ошибка: {e}")


if __name__ == "__main__":
    main()