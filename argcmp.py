from functools import cmp_to_key
from math import atan2

def sign(p):
        if p[0] == 0 and p[1] == 0:
            return 0
        if p[1] < 0 or (p[1] <= 0 and p[0] < 0):
            return -1
        return 1

def argcmp(p0, p1):
    s0 = sign(p0); s1 = sign(p1)
    if s0 != s1:
        return 1 if s0 < s1 else -1
    else:
        return 1 if p1[0]*p0[1] > p0[0]*p1[1] else -1
    
pts = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

pts.sort(key=cmp_to_key(argcmp))
print(pts)
print([sign(p) for p in pts])
print([atan2(p[1], p[0]) for p in pts])

# pts.sort(key=lambda p: atan2(p[1], p[0]))