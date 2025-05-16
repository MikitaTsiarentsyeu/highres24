def justify_text(input_file, output_file, max_chars):
    with open(input_file, 'r') as file:
        text = file.read()

    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_line and current_length + len(word) + len(current_line) > max_chars:
            total_spaces = max_chars - current_length
            gaps = len(current_line) - 1
            space_per_gap, extra_spaces = divmod(total_spaces, gaps)

            line = ''
            for i, word in enumerate(current_line):
                line += word
                if i < gaps:
                    line += ' ' * (space_per_gap + (1 if i < extra_spaces else 0))
            lines.append(line)

            current_line = []
            current_length = 0

        current_line.append(word)
        current_length += len(word)

    if current_line:
        lines.append(' '.join(current_line))

    with open(output_file, 'w') as file:
        file.write('\n'.join(lines))

input_file = 'C:/Users/nstep/Desktop/school of digital competencies/S2/2025 HR S2 Algorithms and DS/practice/highres24/assignments/24-HR-JA/homework 9/stepanenko/input.txt'
output_file = 'C:/Users/nstep/Desktop/school of digital competencies/S2/2025 HR S2 Algorithms and DS/practice/highres24/assignments/24-HR-JA/homework 9/stepanenko/output.txt'
max_chars = int(input("Enter the maximum number of characters per line (must be greater than 20): "))

if max_chars > 20:
    justify_text(input_file, output_file, max_chars)
    print(f"Text has been justified and saved to {output_file}")
else:
    print("Maximum number of characters per line must be greater than 20.")
