def justify(text:str,max):
    justifiedLines = []
    words = text.split()
    currentLineWords=[]
    currentLineLength=0
    for word in words:
        if(len(word)>max):
            if(currentLineWords):
                justifiedLines.append(justifyLine(currentLineWords))
            justifiedLines.append(word)
        elif(currentLineLength+len(word)<=max):
            currentLineWords.append(word)
            currentLineLength+=len(word)+2
        else:
            justifiedLines.append(justifyLine(currentLineWords,max))
            currentLineWords=[word]
            currentLineLength=len(word)+1
    if(currentLineWords):
        justifiedLines.append(justifyLine(currentLineWords,max))
    return '\n'.join(justifiedLines)

def justifyLine(words:list,max):
    if(len(words)==1):
        return words[0]
    out = ''
    neededSpaces = max - sum([len(word) for word in words])
    spacesPerWord = neededSpaces//(len(words)-1)
    additionalSpaces = neededSpaces%(len(words)-1)
    for i,word in enumerate(words):
        out+=word
        out+=" "*(spacesPerWord+(1 if i<additionalSpaces else 0))
    return out

print(justify('''Epistemology is the branch of philosophy that examines the nature, origin, and limits of
               knowledge. It investigates various types of knowledge, including theoretical and practical
               knowledge, and related concepts, such as belief, truth, and justification. Epistemologists
               distinguish different sources of knowledge, ranging from perception and introspection to memory,
               reason, and testimony. The schools of skepticism and fallibilism question the existence and
               certainty of knowledge, while empiricism and rationalism debate whether all knowledge stems
               from sense experience. Theories discussing the nature and role of justification include
               foundationalism, coherentism, internalism, and externalism. Separate branches of epistemology
               focus on knowledge in specific fields, such as scientific, mathematical, moral, and religious
               knowledge. Other branches are characterized by the aspects of knowledge they investigate or the
               research methodologies they use. Early reflections on the nature, sources, and scope of knowledge
               are found in ancient Greek, Indian, and Chinese philosophy.''', 20))