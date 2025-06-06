def justifyLine(line, targetLength):
    words = line.split()
    if len(words) == 1:
        return words[0].ljust(targetLength)
    total_length = sum(len(word) for word in words)
    total_spaces = targetLength - total_length
    space_slots = len(words) - 1
    base_space = total_spaces // space_slots
    extra = total_spaces % space_slots

    line = ""
    for i in range(space_slots):
        line += words[i] + " " * (base_space + (1 if i < extra else 0))
    line += words[-1]
    return line


def justifyText(lineLength):
    lineLength = int(lineLength)
    if lineLength < 20:
        raise ValueError("Line length must be at least 20.")

    with open("text.txt", "r") as file:
        text = file.read()

    paragraphs = text.strip().split("\n\n")
    justifiedParagraphs = []

    for paragraph in paragraphs:
        words = paragraph.split()
        lines = []
        currentLineWords = []
        currentLineLength = 0

        for word in words:
            if len(word) > lineLength:
                raise ValueError(f"Word too long for line: {word}")

            if currentLineLength + len(word) + len(currentLineWords) > lineLength:
                line = justifyLine(" ".join(currentLineWords), lineLength)
                lines.append(line)
                currentLineWords = [word]
                currentLineLength = len(word)
            else:
                currentLineWords.append(word)
                currentLineLength += len(word)

        justifiedParagraphs.append("\n".join(lines))

    with open("result.txt", "w") as file:
        file.write("\n\n".join(justifiedParagraphs))
