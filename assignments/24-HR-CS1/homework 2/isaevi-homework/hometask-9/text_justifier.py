def justify_line(words, width):
    if len(words) == 1:
        return words[0]
    
    total_spaces = width - sum(len(word) for word in words)
    gaps = len(words) - 1
    
    if gaps == 0:
        return words[0]
    
    base_spaces = total_spaces // gaps
    extra_spaces = total_spaces % gaps
    
    justified_line = words[0]
    for i in range(1, len(words)):
        spaces = base_spaces + (1 if i <= extra_spaces else 0)
        justified_line += ' ' * spaces + words[i]
    
    return justified_line

def justify_text(text, width):
    text = ' '.join(text.split())
    words = text.split()
    
    lines = []
    current_line = []
    current_length = 0
    
    for word in words:
        new_length = current_length + len(word)
        if current_line:
            new_length += 1
            
        if new_length > width:
            if current_line:
                justified = justify_line(current_line, width)
                lines.append(justified)
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length = new_length
    
    if current_line:
        if len(current_line) == 1:
            lines.append(current_line[0])
        else:
            last_line = justify_line(current_line, width)
            lines.append(last_line)
    
    return '\n'.join(lines)

def main():
    try:
        with open('input_text.txt', 'r', encoding='utf-8') as file:
            text = file.read().strip()
            if not text:
                print("Error: input file is empty!")
                return
    except FileNotFoundError:
        print("Error: input_text.txt not found!")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return
    
    while True:
        try:
            width = int(input("Enter maximum number of characters per line (must be greater than 20): "))
            if width > 20:
                break
            print("Width must be greater than 20!")
        except ValueError:
            print("Please enter a valid number!")
    
    justified_text = justify_text(text, width)
    
    if not justified_text:
        print("Error: No text to display!")
        return
    
    print("\nJustified text:")
    print("-" * width)
    print(justified_text)
    print("-" * width)

if __name__ == "__main__":
    main() 