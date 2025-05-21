def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2

def calculate(expression):
    try:
        expression = expression.replace(" ", "")

        if '+' in expression:
            parts = expression.split('+')
            if len(parts) == 2:
                num1_str, num2_str = parts
                return add(float(num1_str), float(num2_str))
            else:
                return "Error! Invalid addition format."
        elif '-' in expression:
            parts = expression.split('-')
            if len(parts) == 2:
                num1_str, num2_str = parts
                return subtract(float(num1_str), float(num2_str))
            else:
                return "Error! Invalid subtraction format."
        elif '*' in expression:
            parts = expression.split('*')
            if len(parts) == 2:
                num1_str, num2_str = parts
                return multiply(float(num1_str), float(num2_str))
            else:
                return "Error! Invalid multiplication format."
        elif '/' in expression:
            parts = expression.split('/')
            if len(parts) == 2:
                num1_str, num2_str = parts
                return divide(float(num1_str), float(num2_str))
            else:
                return "Error! Invalid division format."
        else:
            try:
                return float(expression) 
            except ValueError:
                return "Error! Invalid input."

    except Exception as e:
        return f"An unexpected error occurred: {e}"

while True:
    user_input = input("Enter a simple mathematical expression (e.g., 2+3, 5-1, 4*2, 6/3) or type 'quit' to exit: ")
    if user_input.lower() == 'quit':
        print("Goodbye!")
        break
    else:
        result = calculate(user_input)
        print("Result:", result)