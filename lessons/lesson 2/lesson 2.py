import decimal

x = 10
x = "test"

print(type(10))

print((2**10)**0.5)

print(10/5, 10//5)
print(12/5, 12//5)

print(type(2.0))

print(0.1+0.1+0.1)

print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1'))

print(True, False, type(True))

print(True and False, True or False, not False)

print(True == 1, False == 0)
print(True + True + True)

print(bool("test"))
print(bool(""))

print(5 or "test")
print("test" or 5)
print("test" and 5)

print("left") and print("right")
# res = print("test")
# print(res, type(res))

s = 'a'
print(type(s))

s = "a"
print(type(s))

s = '''a'''
s = """a"""

s = '''line 1
line 2
line 3'''

print(s)
print(repr(s))

print(1,2,3,4,5,6,7,8,9)

x = input("Enter your int value:\n")
print(x, type(x))

x = int(x)
print(x, type(x))