class Calculator:
    def __init__(self):
        self.operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def tokenize(self, expression):
        tokens = []
        current_number = ''
        
        for char in expression:
            if char.isspace():
                continue
                
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ''
                if char in self.operators or char in '()':
                    tokens.append(char)
                    
        if current_number:
            tokens.append(float(current_number))
            
        return tokens

    def to_postfix(self, tokens):
        output = []
        operator_stack = []
        
        for token in tokens:
            if isinstance(token, (int, float)):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            else:
                while (operator_stack and operator_stack[-1] != '(' and 
                       self.precedence.get(operator_stack[-1], 0) >= self.precedence.get(token, 0)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
                
        while operator_stack:
            output.append(operator_stack.pop())
            
        return output

    def evaluate_postfix(self, postfix):
        stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands")
                b = stack.pop()
                a = stack.pop()
                try:
                    result = self.operators[token](a, b)
                    stack.append(result)
                except ZeroDivisionError:
                    raise ValueError("Error: Division by zero")
                except Exception as e:
                    raise ValueError(f"Error during calculation: {str(e)}")
                    
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
            
        return stack[0]

    def calculate(self, expression):
        try:
            tokens = self.tokenize(expression)
            if not tokens:
                raise ValueError("Empty expression")
                
            postfix = self.to_postfix(tokens)
            return self.evaluate_postfix(postfix)
            
        except ValueError as e:
            raise ValueError(str(e))
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

def main():
    calculator = Calculator()
    print("Welcome to the Calculator!")
    print("Enter 'quit' to exit")
    print("Supported operations: +, -, *, /, and parentheses ()")
    
    while True:
        try:
            expression = input("\nEnter an expression: ").strip()
            
            if expression.lower() == 'quit':
                print("Goodbye!")
                break
                
            if not expression:
                print("Please enter a valid expression")
                continue
                
            result = calculator.calculate(expression)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {str(e)}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except Exception as e:
            print(f"Unexpected error: {str(e)}")

if __name__ == "__main__":
    main()