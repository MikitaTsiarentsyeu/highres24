class Dictionary:
    def __init__(self, capacity=8):
        self._buckets = [[] for _ in range(capacity)]
        self._size = 0

    def _bucket_index(self, key):
        return hash(key) % len(self._buckets)

    def put(self, key, value):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self._size += 1

    def get(self, key):
        idx = self._bucket_index(key)
        for k, v in self._buckets[idx]:
            if k == key:
                return v
        raise KeyError(key)

    def remove(self, key):
        idx = self._bucket_index(key)
        bucket = self._buckets[idx]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                self._size -= 1
                return
        raise KeyError(key)

    def contains_key(self, key):
        idx = self._bucket_index(key)
        return any(k == key for k, _ in self._buckets[idx])

    def contains_value(self, value):
        return any(v == value for bucket in self._buckets for _, v in bucket)

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def __repr__(self):
        items = ", ".join(f"{k}: {v}" for b in self._buckets for k, v in b)
        return f"Dictionary({{{items}}})"

# Я реализовала его через массив списков.
# Для каждого ключа я вычисляю хэш и ищу значение в нужном списке по индексу.

# put(key, value):
#   добавляет новую пару или обновляет существующую

# get(key):
#   возвращает значение по ключу или вызывает KeyError, если нет

# remove(key):
#   удаляет пару по ключу, если найдена

# contains_key(key):
#   проверяет, есть ли ключ в словаре

# is_empty():
#   проверяет, пустой ли словарь

# __len__():
#   возвращает количество пар (ключ-значение)

# __repr__():
#   выводит все пары словаря как строку — удобно для print(dictionary)