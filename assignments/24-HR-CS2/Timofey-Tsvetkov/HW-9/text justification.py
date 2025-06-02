import os

def get_file_path(filename):
    """Get absolute path to file in the same directory as the script"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, filename)

def read_text_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read().split()
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        print("Please make sure:")
        print(f"1. The file exists in: {os.path.dirname(file_path)}")
        print("2. The filename is correct (including .txt extension)")
        raise
    except Exception as e:
        print(f"Error reading file: {e}")
        raise

def justify_text(words, width):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_line and current_length + len(word) + len(current_line) > width:
            lines.append(justify_line(current_line, width))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))
    return lines

def justify_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)
    
    total_chars = sum(len(word) for word in words)
    total_spaces = width - total_chars
    gaps = len(words) - 1
    spaces = [' ' * (total_spaces // gaps + (1 if i < total_spaces % gaps else 0)) 
             for i in range(gaps)]
    return ''.join(word + (spaces[i] if i < len(spaces) else '') 
                  for i, word in enumerate(words))

def main():
    MIN_WIDTH = 20
    input_file = get_file_path("input.txt")
    output_file = get_file_path("output.txt")

    print(f"Looking for input.txt in: {os.path.dirname(input_file)}")
    
    try:
        while True:
            try:
                width = int(input(f"Enter max characters per line (>{MIN_WIDTH}): "))
                if width > MIN_WIDTH:
                    break
                print(f"Must be greater than {MIN_WIDTH}")
            except ValueError:
                print("Please enter a number")

        words = read_text_file(input_file)
        justified_lines = justify_text(words, width)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(justified_lines))
        
        print(f"Success! Output saved to:\n{output_file}")

    except Exception as e:
        print(f"Program failed: {e}")
        print("Check that input.txt exists in the same folder as this script")

if __name__ == "__main__":
    main()