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

print(justify(''' Эпистемология - философско-методологическая дисциплина, исследующая знание как таковое,
               его строение, структуру, функционирование и развитие. 
              Нередко (особенно в английском языке) слово выступает как синоним гносеоло́гии..''', 20))