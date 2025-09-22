def heron(a, b, c):
    s = (a + b + c) / 2

    res = s * (s-a) * (s-b) * (s-c)

    return res ** 0.5