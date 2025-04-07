test = "global"

def tes_scopes(test):
    test = 5
    print(test)

p = "p"
tes_scopes(p)
print(p, test)

l=[]

def modify_list():
    l.append(10)

modify_list()
print(l)