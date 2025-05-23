def stretch_spaces(words, max_len):
    if len(words) == 1:
        return words[0].ljust(max_len)

    total_word_length = sum(len(word) for word in words)
    total_spaces = max_len - total_word_length
    gaps = len(words) - 1
    base_space = total_spaces // gaps
    extra = total_spaces % gaps

    result = ""
    for i in range(gaps):
        result += words[i]
        result += " " * (base_space + (1 if i < extra else 0))
    result += words[-1]

    return result


def align_text_to_width(text, width):
    words = text.split()
    lines = []
    line_words = []
    line_length = 0

    for word in words:
        if line_length + len(word) + len(line_words) > width:
            lines.append(stretch_spaces(line_words, width))
            line_words = [word]
            line_length = len(word)
        else:
            line_words.append(word)
            line_length += len(word)
    if line_words:
        last_line = ' '.join(line_words).ljust(width)
        lines.append(last_line)

    return lines

def main():
    try:
        max_chars = int(input("Enter line width (minimum 20): "))
        if max_chars <= 20:
            raise ValueError
    except:
        print("Invalid input. Must be a number > 20.")
        return

    try:
        f = open("text.txt", "r", encoding="utf-8")
        text = f.read()
        f.close()
    except:
        print("Could not open 'text.txt'.")
        return

    result_lines = align_text_to_width(text, max_chars)

    out = open("formatted.txt", "w", encoding="utf-8")
    for line in result_lines:
        out.write(line + "\n")
    out.close()

    print("Justified text saved to 'formatted.txt'")

if __name__ == "__main__":
    main()
