class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        self._data.append(item)

    def pop(self):
        if not self._data:
            raise IndexError('pop from empty stack')
        return self._data.pop()

    def peek(self):
        if not self._data:
            raise IndexError('peek from empty stack')
        return self._data[-1]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Stack({self._data})"

# Я реализовала его на обычном списке, вручную написала нужные методы.

# push(item): добавляет элемент наверх стека
# pop(): удаляет и возвращает верхний элемент (ошибка, если стек пуст)
# peek(): просто смотрит на верхний элемент
# is_empty(): проверяет, пуст ли стек
# __len__(): возвращает количество элементов
# __repr__(): выводит стек через print()