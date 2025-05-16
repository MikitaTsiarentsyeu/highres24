def justify_line(words, width):
    if len(words) == 1:
        return words[0].ljust(width)

    total_chars = sum(len(word) for word in words)
    total_spaces = width - total_chars
    gaps = len(words) - 1
    spaces = [' ' * (total_spaces // gaps + (1 if i < total_spaces % gaps else 0)) for i in range(gaps)]
    line = ''.join(word + (spaces[i] if i < len(spaces) else '') for i, word in enumerate(words))
    line += words[-1]
    return line

def justify_text(text, width):
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > width:
            lines.append(justify_line(current_line, width))
            current_line = [word]
            current_length = len(word)
        else:
            current_line.append(word)
            current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))

    return lines

def main():
    input_path = 'input.txt'
    output_path = 'output.txt'

    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print("Ошибка: файл 'input.txt' не найден.")
        return

    try:
        width = int(input("Введите максимально допустимую длину строки (>20): "))
        if width <= 20:
            print("Ошибка: ширина должна быть больше 20.")
            return
    except ValueError:
        print("Ошибка: введите число.")
        return

    justified_lines = justify_text(text, width)

    with open(output_path, 'w', encoding='utf-8') as file:
        for line in justified_lines:
            file.write(line + '\n')

    print(f"Форматированный текст записан в '{output_path}'.")