import os

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()
    
def write_text_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

def justify_line(words, max_length):
    if len(words) == 1:
        return words[0].ljust(max_length)
    
    total_chars = sum(len(word) for word in words)
    space_nedeed = max_length - total_chars
    gaps = len(words) - 1
    space_width, extra = divmod(space_nedeed, gaps)
    
    justified = ''
    for i, word in enumerate(words[:-1]):
        justified += word + ' ' * (space_width + (1 if i < extra else 0))
    justified += words[-1]
    return justified

def justify_text(text, max_chars):
    words = text.split()
    result_lines = []
    current_line = []
    current_len = 0

    for word in words:
        if current_len + len(current_line) + len(word) > max_chars:
            result_lines.append(justify_line(current_line, max_chars))
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word)
    
    if current_line:
        result_lines.append(' '.join(current_line).ljust(max_chars))

    return '\n'.join(result_lines)

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    input_path = os.path.join(base_dir, 'sample_text.txt')
    output_path = os.path.join(base_dir, 'justified_output.txt')

    try:
        max_chars = int(input("Enter maximum number of characters per line (> 20): "))
        if max_chars <= 20:
            print("The value must be greater than 20.")
            return
    except ValueError:
        print("Please enter a valid integer.")
        return
    
    text = read_text_file(input_path)
    justified = justify_text(text, max_chars)
    write_text_file(output_path, justified)
    print(f"Justified text has been saved to '{output_path}'.")

if __name__ == '__main__':
    main()

