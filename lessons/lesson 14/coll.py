

class MyTestColl:

    def __init__(self, *args):
        self.__container = []
        if args:
            self.__container.extend(args)

    def append(self, value):
        self.__container.append(value)

    def remove(self, value):
        try:
            self.__container.remove(value)
        except ValueError:
            raise ValueError(f"value not in {self.__class__.__name__}")

    def __str__(self):
        if self.__container:
            return f"{self.__class__.__name__}({','.join(map(str, self.__container))})"
        else:
            return f"{self.__class__.__name__}()"
        
    def __len__(self):
        return len(self.__container)
    
    def __contains__(self, value):
        return value in self.__container
    
    def __getitem__(self, index):
        try:
            return self.__container[index]
        except IndexError:
            raise IndexError(f"{self.__class__.__name__} index out of range")
    
    def __setitem__(self, index, value):
        try:
            self.__container[index] = value
        except IndexError:
            raise IndexError(f"{self.__class__.__name__} index out of range")
    
    def __iter__(self):
        # self.__hidden_iter = iter(self.__container)
        # return self.__hidden_iter
        self.__iter_index = 0
        return self

    def __next__(self):
        try:
            value = self.__container[self.__iter_index]
        except IndexError:
            # del self.__iter_index
            raise StopIteration
        self.__iter_index += 1
        return value

    
mtc = MyTestColl(1, 2, 3)
print(mtc)

mtc.append("test")
print(mtc)

mtc.remove(1)
print(mtc)

# mtc.remove(111)
        
print(mtc[0])

mtc[0] = "one"
print(mtc[0])


for i in mtc:
    print(i)


print(hash("test"))

def my_hash(x):
    return len(x)

print(my_hash("test"), my_hash("rest"))