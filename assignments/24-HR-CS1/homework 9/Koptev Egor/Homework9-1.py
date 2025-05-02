def LineSpaceExchange(words, max_length): #Exchange space between words in one line
    if len(words) == 1: #If one word in line -> add enough space after it.
        return words[0].ljust(max_length)

    total_chars = sum(len(word) for word in words) #Number of chars in all words
    total_spaces = max_length - total_chars #Number of spaces required
    gaps = len(words) - 1 #Number of gaps between all words
    space_between = total_spaces // gaps #Exchange space between gaps
    extra = total_spaces % gaps #Number of remaining spaces

    justified = ''
    for gap_index in range(len(words) - 1): #Checking all words except last
        word = words[gap_index] #Take specific word
        if gap_index < extra: #Need to add extra space?
            spaces_to_add = space_between + 1
        else:
            spaces_to_add = space_between
        justified += word + (' ' * spaces_to_add) #Add word and required spaces
    justified += words[-1] #Add last word without space
    return justified

def TextSpaceExchange(text, max_length):
    words = text.split() #Text to words
    lines = []
    current_line = []
    current_len = 0

    for word in words:
        if current_len + len(current_line) + len(word) > max_length: #add the new word to the string and check it. if length is not enough
            lines.append(LineSpaceExchange(current_line, max_length)) #Justify finished line
            current_line = [word] #New array of strings with new word
            current_len = len(word) #Length of word
        else: # if length is enough -> add new word
            current_line.append(word) #Add new word to ends of string
            current_len += len(word) #Increase the length of string

    if current_line: #If after "for" words still exist in string
        last_line_text = ' '.join(current_line) #Combine all remaining words in one line with one space
        padded_last_line = last_line_text.ljust(max_length) #Align the last line to the left, adding spaces to the right
        lines.append(padded_last_line) #Add this line to the general list of lines

    return '\n'.join(lines) #All string to text

def main():
    with open('text.txt', 'r', encoding='utf-8') as file:  #Read text from file
        text = file.read()

    max_len = int(input("Enter maximum number of characters per line: "))

    justified = TextSpaceExchange(text, max_len)
    output_file = 'justified_text.txt'

    with open(output_file, 'w', encoding='utf-8') as file: #Write json
        file.write(justified)

main()