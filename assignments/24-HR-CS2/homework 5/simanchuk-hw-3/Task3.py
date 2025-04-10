# Task 3 - Kick out members of a list
# Write a function to kick out elements of a list by value, all encounters, modification in-place

def kick_out(l: list, val: object) -> None: 
    i = 0
    while i < len(l):
        if l[i] == val:
            l.pop(i)
        else:
            i +=1

normLang = ["JS", "C#", "C", "Python", "PascalABC", "1C"]

kick_out(normLang, "JS")
kick_out(normLang, "PascalABC")
print(normLang)