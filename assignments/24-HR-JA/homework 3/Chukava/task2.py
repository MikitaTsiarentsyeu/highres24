import math
import re

s = input()
s = s.replace(" ", "")

match = re.fullmatch(r'([+-]?\d*\.?\d*)x\*x([+-]\d*\.?\d*)x([+-]\d*\.?\d*)=0', s)
if not match:
    print("invalid input")
else:
    def parse(c):
        return float(c) if c not in ("", "+", "-") else float(c + "1")

    a, b, c = map(parse, match.groups())

    if a == 0:
        pass
    else:
        d = b**2 - 4*a*c
        if d > 0:
            x1 = (-b + math.sqrt(d)) / (2*a)
            x2 = (-b - math.sqrt(d)) / (2*a)
            print(x1, x2)
        elif d == 0:
            x = -b / (2*a)
            print(x)
        else:
            print("no solution")