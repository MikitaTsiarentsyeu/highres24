def load_terms_from_document(doc_name):
    with open(doc_name, 'r', encoding='utf-8') as doc:
        return doc.read().split()


def build_aligned_row(terms, row_length):
    if len(terms) == 1:
        return terms[0].ljust(row_length)

    total_chars = sum(len(term) for term in terms)
    total_gap = row_length - total_chars
    gap_positions = len(terms) - 1

    gap_allocation = [' ' * (total_gap // gap_positions + (1 if i < total_gap % gap_positions else 0))
                      for i in range(gap_positions)]

    aligned = ''.join(
        term + (gap_allocation[i] if i < len(gap_allocation) else '')
        for i, term in enumerate(terms)
    )
    return aligned


def align_content(terms, row_length):
    output_rows = []
    temp_list = []
    temp_size = 0

    for term in terms:
        if temp_size + len(term) + len(temp_list) > row_length:
            output_rows.append(build_aligned_row(temp_list, row_length))
            temp_list = [term]
            temp_size = len(term)
        else:
            temp_list.append(term)
            temp_size += len(term)

    if temp_list:
        output_rows.append(' '.join(temp_list).ljust(row_length))

    return output_rows


def save_to_document(lines, out_doc_name):
    with open(out_doc_name, 'w', encoding='utf-8') as out_doc:
        for line in lines:
            out_doc.write(line + '\n')


def execute_aligner(min_chars=21):
    input_doc = 'input.txt'
    output_doc = 'output.txt'

    try:
        line_limit = int(input("Set maximum characters per row (>20): "))
        if line_limit < min_chars:
            print(f" Warning: value must exceed {min_chars - 1}.")
            return
    except ValueError:
        print("Please provide a valid number.")
        return

    try:
        terms = load_terms_from_document(input_doc)
    except FileNotFoundError:
        print(f"Document '{input_doc}' missing.")
        return

    aligned_result = align_content(terms, line_limit)
    save_to_document(aligned_result, output_doc)
    print(f"Complete! Aligned text saved to '{output_doc}'.")


if __name__ == "__main__":
    execute_aligner()