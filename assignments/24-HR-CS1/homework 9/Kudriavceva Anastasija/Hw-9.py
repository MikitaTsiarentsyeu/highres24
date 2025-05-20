import os

def justify_line(words, max_width):
    if len(words) == 1:
        return words[0] + ' ' * (max_width - len(words[0]))

    total_chars = sum(len(word) for word in words)
    total_spaces = max_width - total_chars
    gaps = len(words) - 1

    space_between, extra = divmod(total_spaces, gaps)

    line = ""
    for i, word in enumerate(words):
        line += word
        if i < gaps:
            line += ' ' * (space_between + (1 if i < extra else 0))
    return line

def justify_text(text, max_width):
    words = text.split()
    lines = []
    current_line = []
    current_len = 0

    for word in words:
        if current_len + len(word) + len(current_line) > max_width:
            lines.append(justify_line(current_line, max_width))
            current_line = []
            current_len = 0
        current_line.append(word)
        current_len += len(word)

    # poslednyaya stroka (ne vyrovnivaetsya po shirine)
    last_line = ' '.join(current_line)
    lines.append(last_line + ' ' * (max_width - len(last_line)))

    return '\n'.join(lines)

try:
    # Pechat' tekushchego kataloga (dlya proverki)
    print("Tekushchaya papka:", os.getcwd())

    # Smena direktorii (ukazh zdes' svoy put')
    os.chdir('../highres24/assignments/24-HR-CS1/homework 9/Kudriavceva Anastasija')
    print("Pereshli v papku:", os.getcwd())

    with open('input.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    max_width = int(input("Vvedite maksimal'no dopustimuyu dlinu stroki (>20): "))
    if max_width <= 20:
        print("Oshibka: dlinna dolzhna byt' bol'she 20.")
        exit()

    justified = justify_text(text, max_width)

    with open('output.txt', 'w', encoding='utf-8') as file:
        file.write(justified)

    print("Formatirivannyy tekst zapisali v 'output.txt'")

except FileNotFoundError:
    print("Oshibka: fayl 'input.txt' ne nayden.")
except ValueError:
    print("Oshibka: vvedite chislo (tseloe i >20).")
