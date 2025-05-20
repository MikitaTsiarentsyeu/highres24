import os

def justify_text(words, max_width):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= max_width:
            current_line.append(word)
            current_length += len(word)
        else:
            spaces_needed = max_width - current_length
            if len(current_line) > 1:
                space_between_words = spaces_needed // (len(current_line) - 1)
                extra_spaces = spaces_needed % (len(current_line) - 1)
            else:
                space_between_words = spaces_needed
                extra_spaces = 0

            justified_line = ''
            for i in range(len(current_line)):
                justified_line += current_line[i]
                if i < len(current_line) - 1:
                    justified_line += ' ' * (space_between_words + (1 if i < extra_spaces else 0))

            lines.append(justified_line)
            current_line = [word]
            current_length = len(word)

    lines.append(' '.join(current_line))  
    return lines

# Read file ( read optin)
with open('input.txt', 'r', encoding='utf-8') as file:
    text = file.read().split()

max_chars = int(input("Enter max number of characters per line (must be > 20): "))
while max_chars <= 20:
    max_chars = int(input("Please enter a value greater than 20: "))

formatted_lines = justify_text(text, max_chars)

# Write file ( write option )
with open('output.txt', 'w', encoding='utf-8') as file:
    for line in formatted_lines:
        file.write(line + '\n')

print("Text has been justified and saved in 'output.txt'.")
