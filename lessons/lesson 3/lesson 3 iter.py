x = 10

while x > 2:
    if x == 6:
        break
    if x % 2 == 0:
        x = x - 1 
        continue
    print(x)
    x = x - 1
else:
    print("no breaks detected")

# s = "test"

# i = 0
# while i < len(s):
#     print(s[i])
#     i += 1

for elem in [1,2,3,4,5]:
    print(elem)

for elem in "test":
    print(elem)

print(elem)

d =  {"one": 1, "two": 2}

for elem in d:
    print(elem, d[elem])

for key, value in d.items():
    print(key, value)

for i in range(1, 11, 2):
    print(i, end=' ')

print('')

s = "test"

for i in range(len(s)):
    print(s[i])

l = [i for i in range(10)]
print(l)

l = []
for i in range(10):
    l.append(i)
print(l)

print({x:str(x) for x in range(5)})