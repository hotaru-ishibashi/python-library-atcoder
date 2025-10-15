def extgcd(a, b):
    if b:
        d, y, x = extgcd(b, a % b)
        y -= (a // b)*x
        return d, x, y
    return a, 1, 0


def solve_axbyc(a, b, c):
    d, x, y = extgcd(a, b)
    if c%d != 0:
        return None, None
    mul = c // d

    return x*mul, y*mul