#тот класс реализует структуру данных "словарь", в которой можно:
#Добавлять пары ключ–значение.
#Получать значения по ключу.
#Удалять ключи.
#Проверять наличие ключей и значений.

class Dictionary:
    def __init__(self, capacity=8): #capacity=8 - начальное кол-во ячеек в таблице
        self.capacity = capacity #максимальное кол-во ячеек
        self.size = 0 #колво хранящихся ключей
        self.keys = [None] * self.capacity #создаёт список из None длиной self.capacity
        self.values = [None] * self.capacity #создаёт список из None длиной self.capacity
        #self.capacity — это количество «корзин» (buckets), которые ты изначально выделяешь для хранения данных.
        #Массивы keys и values для хранения ключей и значений.
        #Используем параллельные списки: keys[i] соответствует values[i].

    def is_empty(self): #Метод возвращает True, если словарь пустой (нет ни одного ключа).
        return self.size == 0
    
    def _hash(self, key): #получает индекс ключа (от 0 до 7)
        return hash(key) % self.capacity
    
    def _resize(self): #Метод для увеличения таблицы, когда она наполовину заполнена.
        old_keys = self.keys #Сохраняем текущие ключи и значения.
        old_values = self.values #Сохраняем текущие ключи и значения.
        #Увеличиваем размер в 2 раза и создаём новые пустые списки. Обнуляем size, потому что мы будем заново вставлять значения.
        self.capacity *= 2
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity

        #Перезаписываем все старые ключи и значения в новую таблицу с помощью put().
        for i in range(len(old_keys)):
            if old_keys[i] is not None:
                self.put(old_keys[i], old_values[i])

    def put(self, key, value): #Добавление пары ключ–значение в таблицу. Если ключ уже есть, просто обновим значение.
        #Если таблица заполнена на 50% или больше — увеличиваем её.
        if self.size >= self.capacity // 2:
            self._resize()

            #: хеш нужен для скорости и надёжности работы словарей и множеств

        idx = self._hash(key) #Вычисляем индекс, где начать вставку.
        #Если место занято другим ключом — идём дальше (линейный пробинг). Если нашли тот же ключ — обновляем значение.
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                self.values[idx] = value
                return
            idx = (idx + 1) % self.capacity
        #Сохраняем новый ключ и значение.
        self.keys[idx] = key
        self.values[idx] = value
        self.size =+ 1
    
    def get(self, key):#Метод для получения значения по ключу.
        #Ищем индекс, с которого начинать проверку.
        idx = self._hash(key)
        for _ in range(self.capacity):
            #Если нашли ключ — вернули значение. Если встретили None, значит ключа нет.
            if self.keys[idx] is None:
                break
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.capacity
            #Если ничего не нашли — бросаем исключение.
        raise KeyError(f"Key '{key}' not found.")
    
    def remove(self, key): #Метод для удаления ключа и его значения.
        #Если нашли ключ — удалили его и вызвали _rehash_from, чтобы не поломать цепочку поиска. 
        idx = self._hash(key)
        for _ in range(self.capacity):
            if self.keys[idx] is None:
                break
            if self.keys[idx] == key:
                self.keys[idx] = None # означает, что в списке (или другом индексируемом объекте) self.keys на позицию с индексом idx записывается значение None.
                self.values[idx] = None
                self.size -= 1
                self._rehash_from(idx)
                return
            idx = (idx +1) % self.capacity
            #Если не нашли — ошибка.
        raise KeyError(f"Key '{key}' not found.")
    
    def _rehash_from(self, start_idx): #Этот метод перестраивает все элементы, которые могли находиться после удалённого ключа (поднимает след эл-т на место удаленного).
        #Удаляем элемент, уменьшаем счётчик и вставляем его заново с помощью put().
        idx = (start_idx + 1) % self.capacity
        while self.keys[idx] is not None:
            key_to_rehash = self.keys[idx] #означает, что мы извлекаем элемент из структуры данных self.keys по индексу idx и сохраняем его в переменную key_to_rehash.
            val_to_rehash = self.values[idx]
            self.keys[idx] = None
            self.values[idx] = None
            self.size -= 1
            self.put(key_to_rehash, val_to_rehash)
            idx = (idx + 1) % self.capacity
    
    def contains_key(self, key): #Проверка наличия ключа. Если get() не выбросит исключение — ключ есть.
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def contains_value(self, value): #Проверка наличия значения среди всех сохранённых значений.
        return value in [v for v in self.values if v is not None]
