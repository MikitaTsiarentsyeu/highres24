import math
import decimal

xc = 77
print(type(xc))
xc = "test"
print(type(xc))

print(454218784512121548451231225)

print(10//2, 10/2, 12//3)
print(2**5, 144**0.5)

print(math.sqrt(144))

my_pi = 3.14
print(my_pi, math.pi)

print(0.1+0.1+0.1)

print(decimal.Decimal('0.1')+decimal.Decimal('0.1')+decimal.Decimal('0.1'))

print(type(True), type(False))
print(isinstance(True, bool))
print(isinstance(True, int))
print(id(True), id(1))
print(True == 1)
print(True*6)

print(True and False, True or False)
print(5 or "test")
print("test" or 5)

print(not "test")

print("left") and print("right")

print(type('a'))

test_str = "test '''''''''' \"str"
print(repr(test_str))
test_str = 'test """""""""" \'str'
print(repr(test_str))

x = '''line 1
line 2
line 3'''
print(repr(x))

# x = """line 1
# line 2
# line 3"""

print(1,2,3,4,5,6,7,8,9, sep=', ', end='!\n')
print("test")

res = input("Enter your integer value:\n")
print(res, type(res))

res = int(res)
print(res, type(res))

s = f"tes not test {res} {5+5}"
print(s)

print("test "*res)