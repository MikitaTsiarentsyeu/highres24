def justify_line(words, max_width):
    if len(words) == 1:
        return words[0] + ' ' * (max_width - len(words[0]))

    total_letters = sum(len(word) for word in words)
    spaces = max_width - total_letters
    between = len(words) - 1
    space_each = spaces // between
    extra = spaces % between

    line = ''
    for i in range(len(words) - 1):
        line += words[i]
        line += ' ' * space_each
        if i < extra:
            line += ' '
    line += words[-1]
    return line

def justify_text(text, max_width):
    words = text.split()
    result = []
    line = []
    length = 0

    for word in words:
        if length + len(word) + len(line) > max_width:
            result.append(justify_line(line, max_width))
            line = []
            length = 0
        line.append(word)
        length += len(word)

    result.append(' '.join(line)) 
    return '\n'.join(result)

try:
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    max_width = int(input("Введите максимальную длину строки (больше 20): "))
    if max_width <= 20:
        print("Ошибка: длина строки должна быть больше 20.")
    else:
        justified_text = justify_text(text, max_width)
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(justified_text)
        print("Текст выровнен и сохранён в 'output.txt'.")

except FileNotFoundError:
    print("Файл 'input.txt' не найден.")
except ValueError:
    print("Ошибка: введите число.")
