file = open("input.txt", "r", encoding="utf-8")
text = file.read()
file.close()

while True:
    line_width = int(input("Enter max characters per line (> 20): "))
    if line_width > 20:
        break
    print("Must be greater than 20!")

words = text.split()
lines = []
line = []
length = 0


for word in words:
    if length + len(word) + len(line) > line_width:
        spaces_needed = line_width - sum(len(w) for w in line)
        if len(line) == 1:
            lines.append(line[0] + ' ' * spaces_needed)
        else:
            gaps = len(line) - 1
            space = spaces_needed // gaps
            extra = spaces_needed % gaps

            new_line = ''
            for i in range(gaps):
                new_line += line[i]
                new_line += ' ' * (space + (1 if i < extra else 0))
            new_line += line[-1]
            lines.append(new_line)

        line = [word]
        length = len(word)
    else:
        line.append(word)
        length += len(word)

if line:
    lines.append(' '.join(line).ljust(line_width))

f = open("output.txt", "w", encoding="utf-8")
for l in lines:
    f.write(l + "\n")
f.close()

print("Done! Justified text saved to 'output.txt'")