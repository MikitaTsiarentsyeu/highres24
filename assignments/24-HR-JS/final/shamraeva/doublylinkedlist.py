class DoublyLinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        self._size = 0
        if iterable:
            for item in iterable:
                self.append(item)

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def append(self, value):
        new_node = DoublyLinkedList.Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def prepend(self, value):
        new_node = DoublyLinkedList.Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    def _node_at(self, index):
        if index < 0:
            index += self._size
        if index < 0 or index >= self._size:
            raise IndexError('Index out of range')
        if index < self._size // 2:
            node = self.head
            for _ in range(index): node = node.next
        else:
            node = self.tail
            for _ in range(self._size - index - 1): node = node.prev
        return node

    def __getitem__(self, index):
        return self._node_at(index).data

    def __setitem__(self, index, value):
        self._node_at(index).data = value

    def __delitem__(self, index):
        node = self._node_at(index)
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        self._size -= 1

    def delete(self, data):
        try:
            self.remove(data)
        except ValueError:
            pass

    def delete_node(self, node):
        if not isinstance(node, DoublyLinkedList.Node):
            raise TypeError("The argument must be a Node instance")
        
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        self._size -= 1

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

    def remove(self, value):
        current = self.head
        while current and current.data != value:
            current = current.next
        if not current:
            raise ValueError(f"{value} not in list")
        if current.prev:
            current.prev.next = current.next
        else:
            self.head = current.next
        if current.next:
            current.next.prev = current.prev
        else:
            self.tail = current.prev
        self._size -= 1

    def clear(self):
        self.head = None
        self.tail = None
        self._size = 0

    def __contains__(self, value):
        return any(item == value for item in self)

    def __repr__(self):
        return f"DoublyLinkedList([{', '.join(repr(x) for x in self)}])"

# Каждый элемент хранится в узле Node, у которого есть значение,
# а также ссылки на предыдущий и следующий узел.

# append(value):
#   добавляет новый элемент в конец списка

# __getitem__(i), __setitem__(i, val), __delitem__(i):
#   позволяют читать, изменять и удалять элементы по индексу

# remove(value):
#   удаляет первое вхождение указанного значения

# clear():
#   очищает весь список

# __len__():
#   возвращает количество элементов

# __iter__():
#   делает список итерируемым (можно использовать в for)

# __contains__():
#   позволяет проверять наличие значения через 'in'

# __repr__():
#   возвращает читаемое строковое представление списка