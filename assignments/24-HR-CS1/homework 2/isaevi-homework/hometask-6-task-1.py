def custom_sort(iterable, key_func):
    n = len(iterable)
    for i in range(n):
        for j in range(0, n - i - 1):
            if key_func(iterable[j]) > key_func(iterable[j + 1]):
                iterable[j], iterable[j + 1] = iterable[j + 1], iterable[j]
    return iterable

if __name__ == '__main__':
    data = [(341, 52), (19, 21), (30, 15)]
    sorted_data = custom_sort(data, key_func=lambda x: x[1])
    print("Sorted data:", sorted_data)