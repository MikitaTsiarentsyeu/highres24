def calculate():
    """Main calculator function"""
    print("Simple Calculator (type 'quit' to exit)")
    while True:
        try:
            expression = input("Enter expression: ").strip()
            if expression.lower() == 'quit':
                break
            
            if not expression:
                raise ValueError("Empty expression")
            
            result = evaluate_expression(expression)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Division by zero")
        except Exception as e:
            print(f"Unexpected error: {e}")

def evaluate_expression(expr: str) -> float:
    """Evaluate a mathematical expression safely"""
    expr = expr.replace(" ", "")
    

    valid_chars = set("0123456789+-*/().")
    if not all(c in valid_chars for c in expr):
        raise ValueError("Invalid characters in expression")

    if expr.count("(") != expr.count(")"):
        raise ValueError("Unbalanced parentheses")
    
    tokens = tokenize(expr)
    
    return evaluate(tokens)

def tokenize(expr: str) -> list:
    tokens = []
    i = 0
    while i < len(expr):
        if expr[i] in '+-*/()':
            tokens.append(expr[i])
            i += 1
        elif expr[i].isdigit() or expr[i] == '.':
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == '.'):
                j += 1
            tokens.append(expr[i:j])
            i = j
        else:
            raise ValueError(f"Invalid character: {expr[i]}")
    return tokens

def evaluate(tokens: list) -> float:
    while '(' in tokens:
        start = tokens.index('(')
        end = find_matching_paren(tokens, start)
        sub_expr = tokens[start+1:end]
        sub_result = evaluate(sub_expr)
        tokens[start:end+1] = [str(sub_result)]
    
    i = 0
    while i < len(tokens):
        if tokens[i] in '*/':
            left = float(tokens[i-1])
            right = float(tokens[i+1])
            if tokens[i] == '*':
                result = left * right
            else:
                if right == 0:
                    raise ZeroDivisionError
                result = left / right
            tokens[i-1:i+2] = [str(result)]
            i -= 1
        i += 1

    result = float(tokens[0])
    for i in range(1, len(tokens), 2):
        op = tokens[i]
        num = float(tokens[i+1])
        if op == '+':
            result += num
        elif op == '-':
            result -= num
    
    return result

def find_matching_paren(tokens: list, start: int) -> int:
#check for ()
    count = 1
    for i in range(start+1, len(tokens)):
        if tokens[i] == '(':
            count += 1
        elif tokens[i] == ')':
            count -= 1
            if count == 0:
                return i
    raise ValueError("Unbalanced parentheses")

if __name__ == "__main__":
    calculate()