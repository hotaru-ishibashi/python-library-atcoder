from functools import cmp_to_key
from math import atan2
def sort_with_cmp(a: list, cmp):
    n = len(a)
    if n <= 1:
        return a
    mid = n // 2
    left = sort_with_cmp(a[:mid], cmp)
    right = sort_with_cmp(a[mid:], cmp)
    res = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if cmp(left[i], right[j]) == -1:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
    while i < len(left):
        res.append(left[i])
        i += 1
    while j < len(right):
        res.append(right[j])
        j += 1
    return res

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
    
C = [
        (1, 0),
        (1, 1),
        (0, 1),
        (-1, 1),
        (-1, 0),
        (-1, -1),
        (0, -1),
        (1, -1),
    ]

C.sort(key=cmp_to_key(argcmp))
# or
C2 = sort_with_cmp(C, argcmp)
print(C)
print(C2)
print([sign(p) for p in C])
print([atan2(p[1], p[0]) for p in C])

# pts.sort(key=lambda p: atan2(p[1], p[0]))