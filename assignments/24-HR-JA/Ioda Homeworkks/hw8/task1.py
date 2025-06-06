def read_input_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print("Error: File not found.")
        return None


def justify_line(words, max_width):
    if len(words) == 1:
        return words[0].ljust(max_width)

    total_chars = sum(len(word) for word in words)
    total_spaces = max_width - total_chars
    slots = len(words) - 1
    space_between = total_spaces // slots
    extra_spaces = total_spaces % slots

    justified = ''
    for i in range(slots):
        justified += words[i]
        justified += ' ' * (space_between + (1 if i < extra_spaces else 0))
    justified += words[-1]
    return justified


def justify_text(text, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(current_line) + len(word) > max_width:
            lines.append(justify_line(current_line, max_width))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    # Last line (left-aligned, not justified)
    if current_line:
        lines.append(' '.join(current_line).ljust(max_width))

    return '\n'.join(lines)


def main():
    input_path = input("Enter the path to the input text file: ").strip()
    text = read_input_file(input_path)
    if text is None:
        return

    try:
        max_width = int(input("Enter the maximum number of characters per line (>20): "))
        if max_width <= 20:
            print("The number must be greater than 20.")
            return
    except ValueError:
        print("Invalid number.")
        return

    justified = justify_text(text, max_width)

    output_path = "justified_output.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(justified)

    print(f"Justified text written to '{output_path}'.")