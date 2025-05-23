import math

def justifyText(lineLength):
    lineLength = int(lineLength)
    if lineLength < 20: raise(ValueError)

    with open("text.txt", "r") as file:
        text = file.read();
        file.close()
    paragraphs = text.split("\n\n")
    justifiedParagraphs = []
    for paragraph in paragraphs:
        words = paragraph.split(" ")
        lines = []
        currentLine = ""
        for word in words:
            if len(currentLine) + len(word) > lineLength:
                lines.append(justifyLine(currentLine.rstrip(), lineLength))
                currentLine = ""
            currentLine += word + " "
        if len(currentLine.rstrip()) > 0:
            lines.append(currentLine.rstrip())
        justifiedParagraphs.append("\n".join(lines))
    with open("result.txt", "w") as file:
        for paragraph in justifiedParagraphs:
            file.write(paragraph + "\n\n")
        file.close()

def justifyLine(line, needLength):
    words = line.split(" ")
    needSpaces = needLength
    for word in words:
        needSpaces -= len(word)
    justifiedLine = words[0]
    for i in range(1, len(words)):
        justifiedLine += " " * math.ceil(needSpaces / (len(words) - i)) + words[i]
        needSpaces -= math.ceil(needSpaces / (len(words) - i))
    return justifiedLine

charactersPerLine = input("input characters per line number (minimum 20): ")
try:
    justifyText(charactersPerLine)
    print("result was deployed in result.txt")
except ValueError:
    print("Invalid input (not a number or number less than 20)")