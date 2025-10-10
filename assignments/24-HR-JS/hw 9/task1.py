def justify_line(words, width):
    if len(words) == 1:
        return words[0]
        
    total_spaces = width - sum(len(word) for word in words)
    gaps = len(words) - 1
    
    if gaps == 0:
        return words[0]
        
    base_spaces = total_spaces // gaps
    extra_spaces = total_spaces % gaps
    
    result = []
    for i, word in enumerate(words):
        result.append(word)
        if i < gaps:
            spaces = base_spaces + (1 if i < extra_spaces else 0)
            result.append(' ' * spaces)
            
    return ''.join(result)

def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        if current_length + len(word) + len(current_line) <= width:
            current_line.append(word)
            current_length += len(word)
        else:
            if current_line:
                lines.append(justify_line(current_line, width))
            current_line = [word]
            current_length = len(word)
            
    if current_line:
        lines.append(' '.join(current_line))
        
    return '\n'.join(lines)

def main():
    try:
        width = int(input("Enter maximum number of characters per line (must be > 20): "))
        if width <= 20:
            print("Error: Width must be greater than 20")
            return
            
        with open('assignments/24-HR-JS/hw 7/sample_text.txt', 'r') as file:
            text = file.read()
            
        justified_text = justify_text(text, width)
        
        output_file = 'assignments/24-HR-JS/hw 7/justified_text.txt'
        with open(output_file, 'w') as file:
            file.write(justified_text)
            
        print(f"\nText has been justified and saved to: {output_file}")
        
    except ValueError:
        print("Error: Please enter a valid number")
    except FileNotFoundError:
        print("Error: Input file not found")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()