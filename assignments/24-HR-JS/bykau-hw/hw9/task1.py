TEXT = """Lone Pine International was a series of chess tournaments held annually in March or April from 1971 through 1981 in Lone Pine, California. The tournaments were formally known as the Louis D. Statham Masters, named after sponsor Louis D. Statham (1907–1983), an engineer and millionaire inventor of medical instruments who was also a Los Angeles-based chess aficionado. The events were seven- to ten-round Swiss system tournaments, with entrance requirements that made them the strongest recurring Swiss tournaments in the U.S. in the 1980s. Grandmaster Isaac Kashdan served as the tournament director."""

def justify(words, width):
    if len(words) == 1: 
        return words[0]
    total_spaces, gaps_count = width - sum(len(word) for word in words), len(words)-1
    base_spaces, extra_spaces = divmod(total_spaces, gaps_count)
    return ''.join([word + ' '*(base_spaces + (idx < extra_spaces)) for idx, word in enumerate(words[:-1])]) + words[-1]

def process(text, max_width):
    result = []
    for paragraph in text.split('\n\n'):
        current_line, current_length = [], 0
        for word in paragraph.split():
            required_space = current_length + len(word) + (current_length > 0)
            if required_space > max_width:
                result.append(justify(current_line, max_width))
                current_line, current_length = [word], len(word)
            else:
                current_line.append(word)
                current_length += len(word) + (current_length > 0)
        result.append(' '.join(current_line))
    return '\n'.join(result + [''])[:-1]

def main():
    width = int(input("Max line (>20): "))
    while width <= 20:
        width = int(input("Max line (>20): "))
    open('result.txt', 'w').write(process(TEXT, width))
    print("Done: result.txt")

if __name__ == "__main__":
    main()