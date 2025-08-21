
class MyCollection:

    def __init__(self, *args):
        self.__container = []
        if args:
            self.__container.extend(args)


    def add(self, value):
        self.__container.append(value)

    def remove(self, value):
        try:
            self.__container.remove(value)
        except ValueError:
            raise ValueError(f"value not in the {MyCollection.__name__}")

    def __str__(self):
        return f"{MyCollection.__name__}({','.join(map(str, self.__container))})"
    

    def __len__(self):
        return len(self.__container)

    def __contains__(self, value):
        return value in self.__container
    
    def __getitem__(self, index):
        try:
            return self.__container[index]
        except IndexError:
            raise IndexError(f"{MyCollection.__name__} index out of range")

    def __setitem__(self, index, value):
        try:
            self.__container[index] = value
        except IndexError:
            raise IndexError(f"{MyCollection.__name__} index out of range")

    def __iter__(self):
        self.__iteration_index = 0
        return self

    def __next__(self):
        try:
            return self.__container[self.__iteration_index]
        except IndexError:
            raise StopIteration
        finally:
            self.__iteration_index += 1


mc = MyCollection()
print(mc)

mc.add(1)
mc.add("test")
mc.add(True)

print(mc)

mc = MyCollection(1,2,3,4,54)
print(mc)

# mc.remove(100)

print(mc[0])

mc[0] = 0
print(mc[0])

for i in mc:
    print(i)