import math 
def own_sort(iter, key_func):
    _list = list(iter)
    for i in range(len(_list)):
        for j in range(len(_list) - 1 - i):
            if key_func(_list[j]) > key_func(_list[j + 1]):
                _list[j], _list[j + 1] =  _list[j + 1], _list[j]
    return _list

digits = [1,9,3,12,11,6,7,0,8]

print(own_sort(digits, lambda x: x))