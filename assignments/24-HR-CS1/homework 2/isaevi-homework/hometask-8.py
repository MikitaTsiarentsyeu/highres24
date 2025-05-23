import sys

PREC = {'+': 1, '-': 1, '*': 2, '/': 2}

def tokenize(expr: str):
    """Преобразуем строку в список токенов: чисел (float) и символов + - * / ( )"""
    tokens = []
    num = ''
    for ch in expr.replace(' ', ''):
        if ch.isdigit() or ch == '.':
            num += ch
        else:
            if num:
                tokens.append(float(num))
                num = ''
            if ch in '+-*/()':
                tokens.append(ch)
            else:
                raise ValueError(f"Неподдерживаемый символ: '{ch}'")
    if num:
        tokens.append(float(num))
    return tokens

def to_postfix(tokens):
    """Преобразуем инфиксный список токенов в постфиксный (RPN)"""
    out, ops = [], []
    for t in tokens:
        if isinstance(t, float):
            out.append(t)
        elif t in PREC:
            while ops and ops[-1] in PREC and PREC[ops[-1]] >= PREC[t]:
                out.append(ops.pop())
            ops.append(t)
        elif t == '(':
            ops.append(t)
        elif t == ')':
            while ops and ops[-1] != '(':
                out.append(ops.pop())
            if not ops or ops[-1] != '(':
                raise ValueError("Несоответствие скобок")
            ops.pop()
    while ops:
        if ops[-1] in '()':
            raise ValueError("Несоответствие скобок")
        out.append(ops.pop())
    return out

def eval_postfix(rpn):
    """Вычисляем постфиксное выражение"""
    stack = []
    for t in rpn:
        if isinstance(t, float):
            stack.append(t)
        else:
            if len(stack) < 2:
                raise ValueError("Неверная структура выражения")
            b, a = stack.pop(), stack.pop()
            if t == '+':
                stack.append(a + b)
            elif t == '-':
                stack.append(a - b)
            elif t == '*':
                stack.append(a * b)
            elif t == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                stack.append(a / b)
    if len(stack) != 1:
        raise ValueError("Неверная структура выражения")
    return stack[0]

def calculate(expr: str):
    tokens = tokenize(expr)
    rpn = to_postfix(tokens)
    return eval_postfix(rpn)

def main():
    print("Простой калькулятор (+, -, *, /, скобки). Для выхода введите 'exit' или 'quit'.")
    while True:
        try:
            expr = input(">>> ")
        except (EOFError, KeyboardInterrupt):
            print("\nПока!")
            sys.exit()
        if expr.lower() in ('exit', 'quit'):
            print("Пока!")
            break
        if not expr.strip():
            continue
        try:
            res = calculate(expr)
            print(int(res) if res.is_integer() else res)
        except ZeroDivisionError as e:
            print("Ошибка: деление на ноль.")
        except ValueError as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")

if __name__ == "__main__":
    main()
