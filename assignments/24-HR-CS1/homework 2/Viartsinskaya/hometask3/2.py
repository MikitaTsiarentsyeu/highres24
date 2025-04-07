import re
import math

def solve_quadratic():
    print("Quadratic Equation Solver (Hard Way)")
    equation = input("Enter equation (format: ax² + bx + c = 0): ").strip()

    try:
        # Preprocess equation
        eq_clean = equation.replace(' ', '').replace('**', '^').replace('*', '').lower()
        
        # Validate equation format
        if not eq_clean.endswith('=0'):
            raise ValueError("Equation must be in form ax² + bx + c = 0")
            
        left_side = eq_clean.split('=0')[0]
        if not left_side:
            raise ValueError("Empty equation")
            
        # Add leading '+' if needed
        if left_side[0] not in '+-':
            left_side = '+' + left_side
            
        # Split into terms
        terms = re.findall(r'([+-][^+-]*)', left_side)
        if not terms:
            raise ValueError("No valid terms found")
            
        a = b = c = 0.0
        
        for term in terms:
            term = term.lower()
            
            # Handle x² terms
            if 'x^2' in term:
                coeff = term.split('x')[0]
                if coeff in ['+', '-']:
                    coeff += '1'
                a += float(coeff)
                
            # Handle x terms (without exponent)
            elif 'x' in term and '^' not in term:
                coeff = term.split('x')[0]
                if coeff in ['+', '-']:
                    coeff += '1'
                b += float(coeff)
                
            # Handle constants
            else:
                c += float(term)
                
        # Check quadratic validity
        if a == 0:
            raise ValueError("Not a quadratic equation (a=0)")
            
        # Calculate discriminant
        discriminant = b**2 - 4*a*c
        
        # Solve and display results
        if discriminant > 0:
            sqrt_d = math.sqrt(discriminant)
            roots = ((-b + sqrt_d)/(2*a)), ((-b - sqrt_d)/(2*a))
            print(f"Two distinct real roots: {roots[0]:.2f} and {roots[1]:.2f}")
        elif discriminant == 0:
            root = -b / (2*a)
            print(f"One real root (repeated): {root:.2f}")
        else:
            real = -b/(2*a)
            imag = math.sqrt(-discriminant)/(2*a)
            print(f"Two complex roots: {real:.2f} + {imag:.2f}i and {real:.2f} - {imag:.2f}i")
            
    except ValueError as e:
        print(f"Error: {str(e)}")
    except Exception:
        print("Invalid equation format. Please use forms like:")
        print("Examples: 2x²-5x+3=0, 3.5x^2 + 2x =0, x^2-4=0")

solve_quadratic() 