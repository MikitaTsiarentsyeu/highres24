s = float(input("Сколько денег?: "))
p = float(input("Процент?: ")) / 100
i = float(input("На сколько лет?: "))
res = s * (p + 1) ** i
print("Будет:", res)
