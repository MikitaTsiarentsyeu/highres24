def tokenize(expr):
    tokens = []
    num = ''
    for c in expr:
        if c.isdigit() or c == '.':
            num += c
        else:
            if num:
                tokens.append(num)
                num = ''
            if c in '+-*/()':
                tokens.append(c)
            elif c.isspace():
                continue
            else:
                raise ValueError(f"Invalid character: {c}")
    if num:
        tokens.append(num)
    return tokens

def parse(tokens):
    def parse_expr():
        nonlocal i
        val = parse_term()
        while i < len(tokens) and tokens[i] in ('+', '-'):
            op = tokens[i]; i += 1
            val2 = parse_term()
            val = val + val2 if op == '+' else val - val2
        return val

    def parse_term():
        nonlocal i
        val = parse_factor()
        while i < len(tokens) and tokens[i] in ('*', '/'):
            op = tokens[i]; i += 1
            val2 = parse_factor()
            if op == '*':
                val *= val2
            else:
                if val2 == 0:
                    raise ZeroDivisionError("Division by zero")
                val /= val2
        return val

    def parse_factor():
        nonlocal i
        token = tokens[i]
        if token == '(':
            i += 1
            val = parse_expr()
            if i >= len(tokens) or tokens[i] != ')':
                raise ValueError("Missing closing parenthesis")
            i += 1
            return val
        elif token == '-':
            i += 1
            return -parse_factor()
        else:
            i += 1
            try:
                return float(token)
            except:
                raise ValueError(f"Invalid number: {token}")
    i = 0
    result = parse_expr()
    if i != len(tokens):
        raise ValueError("Unexpected token at the end")
    return result

def main():
    while True:
        expr = input("Enter expression (or 'exit'): ").strip()
        if expr.lower() == 'exit':
            break
        try:
            tokens = tokenize(expr)
            result = parse(tokens)
            print("Result:", int(result) if result.is_integer() else result)
        except ZeroDivisionError as zde:
            print("Error:", zde)
        except ValueError as ve:
            print("Input error:", ve)
        except Exception:
            print("Unknown error")

if __name__ == "__main__":
    main()
