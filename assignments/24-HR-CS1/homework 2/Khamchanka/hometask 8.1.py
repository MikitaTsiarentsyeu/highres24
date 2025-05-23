def calculate(expression):
    try:
        return parse_expression(expression.replace(" ", ""))
    except ZeroDivisionError:
        return "Error: divide on 0."
    except Exception as e:
        return f"Error: {e}"

def parse_expression(expr):
    while '(' in expr:
        start = expr.rfind('(')
        end = expr.find(')', start)
        if end == -1:
            raise ValueError("Unavailblae ) .")
        inner = expr[start + 1:end]
        value = parse_expression(inner)
        expr = expr[:start] + str(value) + expr[end + 1:]

    for op in ['+', '-', '*', '/']:
        index = find_main_operator(expr, op)
        if index != -1:
            left = parse_expression(expr[:index])
            right = parse_expression(expr[index + 1:])
            return apply_operator(left, right, op)
    try:
        return float(expr)
    except ValueError:
        raise ValueError(f"Wrong number: {expr}")

def find_main_operator(expr, op):
    depth = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ')': depth += 1
        elif expr[i] == '(': depth -= 1
        elif depth == 0 and expr[i] == op:
            return i
    return -1

def apply_operator(a, b, op):
    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/':
        if b == 0:
            raise ZeroDivisionError
        return a / b

def main():
    print("Simple Calculator. Write 'exit' for final.")
    while True:
        expr = input("Write expression: ")
        if expr.lower() == 'exit':
            print("Bye!")
            break
        result = calculate(expr)
        print("Result:", result)

if __name__ == "__main__":
    main()