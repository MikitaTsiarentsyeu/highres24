import textwrap

def justify_text(text, max_width):
    
    words = text.split()
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) <= max_width:
            current_line.append(word)
            current_length += len(word)
        else:
            if current_line:
                lines.append(current_line)
            current_line = [word]
            current_length = len(word)
    
    if current_line:
        lines.append(current_line)

    result = []
    for i in range(len(lines)):
        line = lines[i]
        if i == len(lines) - 1 or len(line) == 1:
            result.append(" ".join(line))
        else:
            total_chars = sum(len(word) for word in line)
            spaces_needed = max_width - total_chars
            gaps = len(line) - 1  
            
            if gaps == 0:  
                result.append(line[0])
                continue
            
            spaces_per_gap = spaces_needed // gaps
            extra_spaces = spaces_needed % gaps
            
            justified_line = ""
            for j in range(len(line) - 1):
                justified_line += line[j]
                spaces = spaces_per_gap + (1 if j < extra_spaces else 0)
                justified_line += " " * spaces
            justified_line += line[-1]  
            result.append(justified_line)
    
    return result

text = ("PYTHON WAS CREATED IN THE EARLY 1990S BY GUIDO VAN ROSSUM AT STICHTING MATHEMATISCH CENTRUM IN THE NETHERLANDS AS A SUCCESSOR OF A LANGUAGE CALLED ABC. GUIDO REMAINS PYTHON PRINCIPAL AUTHOR, ALTHOUGH IT INCLUDES MANY CONTRIBUTIONS FROM OTHERS. IN 1995, GUIDO CONTINUED HIS WORK ON PYTHON AT THE CORPORATION FOR NATIONAL RESEARCH INITIATIVES IN RESTON, VIRGINIA WHERE HE RELEASED SEVERAL VERSIONS OF THE SOFTWARE. IN MAY 2000, GUIDO AND THE PYTHON CORE DEVELOPMENT TEAM MOVED TO BEOPEN.COM TO FORM THE BEOPEN PYTHONLABS TEAM. IN OCTOBER OF THE SAME YEAR, THE PYTHONLABS TEAM MOVED TO DIGITAL CREATIONS. IN 2001, THE PYTHON SOFTWARE FOUNDATION WAS FORMED, A NON-PROFIT ORGANIZATION CREATED SPECIFICALLY TO OWN PYTHON-RELATED INTELLECTUAL PROPERTY. ZOPE CORPORATION IS A SPONSORING MEMBER OF THE PSF. ALL PYTHON RELEASES ARE OPEN SOURCE. HISTORICALLY, MOST, BUT NOT ALL, PYTHON RELEASES HAVE ALSO BEEN GPL-COMPATIBLE; THE TABLE BELOW SUMMARIZES THE VARIOUS RELEASES.")

paragraphs = text.split(". ")
max_width = 40

for paragraph in paragraphs:
    if paragraph:  
        if paragraph != paragraphs[-1]:
            paragraph += "."

        justified = justify_text(paragraph, max_width)
       
        for line in justified:
            print(line)
        print()  