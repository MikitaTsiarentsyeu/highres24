import os

def justify_line(words, max_width):
    if len(words) == 1:
        return words[0].ljust(max_width)
    total_chars = sum(len(word) for word in words)
    total_spaces = max_width - total_chars
    gaps = len(words) - 1
    space_between_words, extra = divmod(total_spaces, gaps)

    line = ""
    for i, word in enumerate(words):
        line += word
        if i < gaps:
            line += " " * (space_between_words + (1 if i < extra else 0))
    return line

def justify_text(text, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_len = 0
    for word in words:
        if current_len + len(word) + len(current_line) > max_width:
            lines.append(justify_line(current_line, max_width))
            current_line = [word]
            current_len = len(word)
        else:
            current_line.append(word)
            current_len += len(word)

    if current_line:
        lines.append(' '.join(current_line).ljust(max_width))

    return lines

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(BASE_DIR, "input.txt")
output_file = os.path.join(BASE_DIR, "output.txt")
max_chars = int(input("enter letters count: "))
with open(input_file, 'r', encoding='utf-8') as f:
   text = f.read()
justified = justify_text(text, max_chars)

with open(output_file, 'w', encoding='utf-8') as f:
    for line in justified:
       f.write(line + '\n')

print("file saved")