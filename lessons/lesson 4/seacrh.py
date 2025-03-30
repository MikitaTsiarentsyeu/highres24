

l = [23,45,67,8,54,3,2,5]

target = 8

i = 0

while i < len(l):
    if l[i] == target:
        break
    i += 1
else:
    i = -1

print(i)

i = -1

for elem in l:
    i += 1
    if elem == target:
        break
else:
    i = -1

print(i)
    

for i, elem in enumerate(l):
    if elem == target:
        print(i)
        break
else:
    print(-1)
    


s = "dsfghjkfdsfghjkliuytretfghjkoiuytr"

d = {}

for symbol in s:
    if symbol in d:
        d[symbol] += 1
    else:
        d[symbol] = 1

print(d)


l = [3,5,6,8,6,3,2,34,6]

for i in range(len(l)):
    for j in range(len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]

print(l)


text = "Some statement. Another statement!"