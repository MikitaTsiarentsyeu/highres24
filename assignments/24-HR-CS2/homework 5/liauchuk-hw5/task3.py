def own_pop(l: list, val: object): 
    i = 0
    for i in range(0, len(l)):
        if l[i] == val:
            l.pop(i)
        else:
            i +=1
_list = ["apple", "orange", "kiwi", "potato"]
own_pop(_list,"potato")
print(_list)