width = 0
while width <= 20:
    try:
        width = int(input("Максимум символов в строке (>20): "))
    except ValueError:
        width = 0

text = open('input.txt', encoding='utf-8').read().replace('\n', ' ')
words = text.split()

lines = []
current, curr_len = [], 0
for w in words:
    if curr_len + len(w) + len(current) <= width:
        current.append(w)
        curr_len += len(w)
    else:
        lines.append(current)
        current, curr_len = [w], len(w)
if current:
    lines.append(current)

def justify_line(ws):
    if len(ws) == 1:
        return ws[0] + ' '*(width - len(ws[0]))
    total = sum(len(w) for w in ws)
    spaces = width - total
    gaps = len(ws) - 1
    base, extra = divmod(spaces, gaps)
    line = ''
    for i, w in enumerate(ws):
        line += w
        if i < gaps:
            line += ' '*(base + (1 if i < extra else 0))
    return line

justified = []
for i, ln in enumerate(lines):
    if i == len(lines) - 1:
        line = ' '.join(ln)
        line += ' '*(width - len(line))
    else:
        line = justify_line(ln)
    justified.append(line)

with open('output.txt', 'w', encoding='utf-8') as f:
    for l in justified:
        f.write(l + '\n')

print("Готово! Проверьте файл output.txt")