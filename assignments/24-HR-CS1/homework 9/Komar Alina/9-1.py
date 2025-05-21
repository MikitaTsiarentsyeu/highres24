def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split()


def justify_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)

    total_chars = sum(len(word) for word in words)
    total_spaces = width - total_chars
    gaps = len(words) - 1
    spaces = [' ' * (total_spaces // gaps + (1 if i < total_spaces % gaps else 0)) for i in range(gaps)]
    justified = ''.join(word + (spaces[i] if i < len(spaces) else '') for i, word in enumerate(words))
    return justified


def justify_text(words, width):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) >= width:
            lines.append(justify_line(current_line, width))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines


def write_output_file(lines, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        for line in lines:
            file.write(line + '\n')


def main(max_char = 20):
    input_file = 'input.txt'
    output_file = 'output.txt'

    try:
        width = int(input("Enter max number of characters per line (>20): "))
        if width <= 20:
            print(f"Value must be greater than {max_char}.")
            return
    except ValueError:
        print("Please enter a number.")
        return

    words = read_text_file(input_file)
    justified_lines = justify_text(words, width)
    write_output_file(justified_lines, output_file)


if __name__ == "__main__":
    main()
