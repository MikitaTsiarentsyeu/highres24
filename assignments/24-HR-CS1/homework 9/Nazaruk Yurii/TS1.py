import os
def justify_line(words, max_width):
    if len(words) == 1:
        return words[0] + ' ' * (max_width - len(words[0]))
    total_chars = sum(len(word) for word in words)
    spaces_needed = max_width - total_chars
    space_slots = len(words) - 1
    space_width, extra = divmod(spaces_needed, space_slots)
    line = ''
    for i in range(len(words) - 1):
        line += words[i] + ' ' * (space_width + (1 if i < extra else 0))
    line += words[-1]
    return line

def justify_text(text, max_width):
    words = text.split()
    result = []
    line = []
    line_length = 0
    for word in words:
        if line_length + len(word) + len(line) > max_width:
            result.append(justify_line(line, max_width))
            line = []
            line_length = 0
        line.append(word)
        line_length += len(word)
    result.append(' '.join(line))
    return '\n'.join(result)

try:
    print(os.getcwd())
    os.chdir('../highres24/assignments/24-HR-CS1/homework 9/Nazaruk Yurii')
    print(os.getcwd())
    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()
    max_width = int(input("Введите максимально допустимую длину строки (>20): "))
    if max_width <= 20:
        print("Ошибка: максимально допустимая длина строки должна быть больше 20.")
        exit()
    justified = justify_text(text, max_width)
    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(justified)
    print("Форматированный текст записан в output.txt")
except FileNotFoundError:
    print("Ошибка: файл 'input.txt' не найден.")
except ValueError:
    print("Ошибка: введите корректное число.")

