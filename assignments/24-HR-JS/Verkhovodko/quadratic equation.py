def simple(a, b, c):
  d = b*b - 4*a*c
  if d<0:
    print("no roots found")
    return False
  x1 = (-b - d**0.5) / (2*a)
  x2 = (-b + d**0.5) / (2*a)
  if x1==x2:
    print(x1)
  else:
    print(x1, "and", x2)

def complex(s):
  s = s.replace("=0", "")
  elems = s.split("+", 3)
  a = int(elems[0].replace("x*x", ""))
  b = int(elems[1].replace("x", ""))
  c = int(elems[2])
  simple(a, b, c)


str = input()
if "+" in str:
  complex(str)
else:
  a = int(str)
  b = int(input())
  c = int(input())
  simple(a, b, c)
