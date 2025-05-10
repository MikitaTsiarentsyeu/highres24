def custom_sort(iterable, key_func = lambda x: x):
    
    pairs = [(item, key_func(item)) for item in iterable]

    n = len(pairs)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if pairs[j][1] > pairs[j + 1][1]:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
                swapped = True
        if not swapped:
            break
    return [item for item, key in pairs]

iterable1 = ['mfrwqf', 'zgecwvx', 'eck', 'ljymds', 'yrc', 'ogcv', 'pvojivqo', 'mdn', 'dys', 'mnzz', 'cyy', 'ddqaote', 'pgdm', 'xyj', 'zgoxxcq', 'zrkcpcru', 'ymkxwpi', 'vizlpewb', 'pfjtl', 'nzn']

print(custom_sort(iterable1, lambda x: len(x)))

iterable2 = [(2,2),(1,3),(3,1)]

print(custom_sort(iterable2, lambda x: x[1]))
print(custom_sort(iterable2))
