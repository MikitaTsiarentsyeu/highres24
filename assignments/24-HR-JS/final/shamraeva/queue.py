class Queue:
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        self._data.append(item)

    def dequeue(self):
        if not self._data:
            raise IndexError('dequeue from empty queue')
        return self._data.pop(0)

    def peek(self):
        if not self._data:
            raise IndexError('peek from empty queue')
        return self._data[0]

    def is_empty(self):
        return len(self._data) == 0

    def __len__(self):
        return len(self._data)

    def __repr__(self):
        return f"Queue({self._data})"
    
    
# Реализовано с помощью списка, логику написалa вручную.

# enqueue(item): добавляет элемент в конец очереди
# dequeue(): удаляет и возвращает первый элемент (ошибка, если очередь пустая)
# peek(): возвращает первый элемент без удаления
# is_empty(): проверяет, пуста ли очередь
# __len__(): количество элементов
# __repr__(): красиво выводит очередь через print()