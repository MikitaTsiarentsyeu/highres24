import os

try:
    file = open("input.txt", "r", encoding="utf-8")
    text = file.read()
    file.close()
except:
    print("Файл не найден")
    exit()

while True:
    max_len = input("Введите максимальное количество символов, на которые будет разбит текст (>20): ")
    if max_len.isdigit() and int(max_len) > 20:
        max_len = int(max_len)
        break
    else:
        print("Нужно целое число больше 20!")

words = text.split()
lines = []
line_words = []
line_length = 0

for word in words:
    if line_length + len(word) + len(line_words) > max_len:
        total_spaces = max_len - sum(len(w) for w in line_words)
        if len(line_words) == 1:
            line = line_words[0] + " " * total_spaces
        else:
            spaces_between = len(line_words) - 1
            space_size = total_spaces // spaces_between
            extra = total_spaces % spaces_between

            line = ""
            for i in range(spaces_between):
                line += line_words[i]
                line += " " * (space_size + (1 if i < extra else 0))
            line += line_words[-1]
        lines.append(line)
        line_words = [word]
        line_length = len(word)
    else:
        line_words.append(word)
        line_length += len(word)

if line_words:
    last_line = " ".join(line_words)
    lines.append(last_line)

output = "\n".join(lines)
f = open("output.txt", "w", encoding="utf-8")
f.write(output)
f.close()

print("Готово! Результат записан в файл output.txt")