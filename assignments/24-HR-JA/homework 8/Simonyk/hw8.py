def split_formula(expr):
    elements = []
    digit_str = ''
    for symbol in expr:
        if symbol.isdigit() or symbol == '.':
            digit_str += symbol
        elif symbol in '+-><()':
            if digit_str:
                elements.append(float(digit_str))
                digit_str = ''
            elements.append(symbol)
        elif symbol.isspace():
            if digit_str:
                elements.append(float(digit_str))
                digit_str = ''
        else:
            raise ValueError(f"Invalid symbol found: '{symbol}'")
    if digit_str:
        elements.append(float(digit_str))
    return elements

def analyze_formula(elements):
    def analyze_unit(pos):
        if elements[pos] == '(':
            value, pos = analyze_sum_diff(pos + 1)
            if pos >= len(elements) or elements[pos] != ')':
                raise ValueError("Parentheses don't match")
            return value, pos + 1
        elif isinstance(elements[pos], float):
            return elements[pos], pos + 1
        else:
            raise ValueError(f"Unexpected element: {elements[pos]}")

    def analyze_mult_div(pos):
        left, pos = analyze_unit(pos)
        while pos < len(elements) and elements[pos] in ('*', '/'):
            oper = elements[pos]
            right, next_pos = analyze_unit(pos + 1)
            if oper == '*':
                left *= right
            elif oper == '/':
                if right == 0:
                    raise ZeroDivisionError("Cannot divide by zero")
                left /= right
            pos = next_pos
        return left, pos

    def analyze_sum_diff(pos):
        left, pos = analyze_mult_div(pos)
        while pos < len(elements) and elements[pos] in ('+', '-'):
            oper = elements[pos]
            right, next_pos = analyze_mult_div(pos + 1)
            if oper == '+':
                left += right
            elif oper == '-':
                left -= right
            pos = next_pos
        return left, pos

    result, final_pos = analyze_sum_diff(0)
    if final_pos != len(elements):
        raise ValueError("Extra elements at the end")
    return result

def calc_tool():
    print("My Personal Calculator (type 'stop' to end)")
    while True:
        input_str = input("Type your formula: ").strip()
        if input_str.lower() in ('stop', 'end'):
            print("See you next time!")
            break
        try:
            elements = split_formula(input_str)
            outcome = analyze_formula(elements)
            print("Answer:", outcome)
        except ZeroDivisionError as zde:
            print("Math Issue:", zde)
        except ValueError as ve:
            print("Input Issue:", ve)
        except Exception as e:
            print("Something went wrong:", e)