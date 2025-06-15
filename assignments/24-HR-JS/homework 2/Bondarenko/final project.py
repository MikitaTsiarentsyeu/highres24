class Dictionary:
    def __init__(self):
        # Инициализация внутреннего хранилища для ключей и значений
        self._data = {}

    def is_empty(self):
        # Проверяет, пуст ли словарь
        return len(self._data) == 0

    def put(self, key, value):
        # Добавляет пару ключ-значение или обновляет значение, если ключ уже существует
        self._data[key] = value

    def get(self, key):
        # Возвращает значение по ключу или вызывает KeyError, если ключ не найден
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        return self._data[key]

    def remove(self, key):
        # Удаляет пару ключ-значение по ключу или вызывает KeyError, если ключ не найден
        if key not in self._data:
            raise KeyError(f"Key '{key}' not found")
        del self._data[key]

    def contains_key(self, key):
        # Проверяет, существует ли ключ в словаре
        return key in self._data

    def contains_value(self, value):
        # Проверяет, существует ли значение в словаре
        return value in self._data.values()

    def __len__(self):
        # Возвращает количество элементов в словаре
        return len(self._data)


# Пример использования
if __name__ == "__main__":
    my_dict = Dictionary()

    # Добавление элементов
    my_dict.put("name", "Alice")
    my_dict.put("age", 30)
    my_dict.put("city", "New York")

    # Проверка длины словаря
    print(len(my_dict))  # Вывод: 3

    # Удаление элемента
    my_dict.remove("age")

    # Проверка длины после удаления
    print(len(my_dict))  # Вывод: 2

    # Проверка наличия ключа
    print(my_dict.contains_key("name"))  # Вывод: True

    # Проверка наличия значения
    print(my_dict.contains_value("New York"))  # Вывод: True