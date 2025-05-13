def justify_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)

    total_chars = sum(len(word) for word in words)
    total_spaces = width - total_chars
    gaps = len(words) - 1
    base_space = total_spaces // gaps
    extra = total_spaces % gaps

    justified = ''
    for i, word in enumerate(words[:-1]):
        justified += word
        spaces = base_space + (1 if i < extra else 0)
        justified += ' ' * spaces
    justified += words[-1]
    return justified


def justify_text(words, width):
    result = []
    line = []
    line_len = 0

    for word in words:
        if line_len + len(line) + len(word) > width:
            result.append(justify_line(line, width))
            line = [word]
            line_len = len(word)
        else:
            line.append(word)
            line_len += len(word)

    if line:
        result.append(' '.join(line).ljust(width))  # Last line: left-aligned
    return result


def main():
    try:
        with open('input.txt', 'r', encoding='utf-8') as f:
            text = f.read()
    except FileNotFoundError:
        print("Error: 'input.txt' not found.")
        return

    try:
        width = int(input("Enter max line width (> 20): "))
        if width <= 20:
            raise ValueError
    except ValueError:
        print("Invalid width. Must be an integer > 20.")
        return

    words = text.split()
    justified_lines = justify_text(words, width)

    with open('output.txt', 'w', encoding='utf-8') as f:
        for line in justified_lines:
            f.write(line + '\n')

    print(f"Text justified to {width} characters per line.")
    print("Output written to 'output.txt'.")

if __name__ == '__main__':
    main()
