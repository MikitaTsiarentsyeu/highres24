s = "test str"

print(len(s))

print(bool(s), bool(''))

print('test' in s)

print(s[0], s[1], s[-1])

print(s[0:3], s[:3], s[::-1])

# s[0] = 'r' #error

l = [1,2,3,4,5,"test",True]
print(type(l))

l[0] = 1.0
print(l)
print(len(l), 1 in l, l[::-1])

l = list("test")
print(l, type(l))

print(str(l))
print(''.join(l))

print("some every long string".split())

l.append("the last one")
print(l)
l.insert(0, "the first one")
print(l)

l.extend("test")
print(l)

l.remove('t')
print(l)

l.clear()
print(l)

m = l

del l
print(m)

l = [1,2,3,4,5]
del l[0:3]
print(l)

l = [1,2,3,4,5]
l[:3] = [True, False]
print(l)

t = (1,2,3,4,5,"test",True)
print(type(t))

# t[0] = 0 # error

# del t[0] # error

t = (10.1,)
print(type(t))

t = 1,2,3,4,5
print(type(t))

a, b = 3, 4
print(a, b)

a, b = b, a
print(a, b)

d = {}
print(d, type(d))

d = {"one": 1, "two": 2}
print(d, type(d))

print(d["one"])
d["one"] = 1.1111111

print(d["one"])

d[3] = "three"
print(d)

print(len(d), 2 in d, 3 in d)

print(2 in d.values(), list(d.values()))

s = {1,1,1,1,1,1,1,1,1,1,2,3,4,6,True,"test"}
print(s, type(s))

print(set("ytrutyfuyfutdytdytytyt"))