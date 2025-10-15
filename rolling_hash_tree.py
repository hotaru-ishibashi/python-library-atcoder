from atcoder.segtree import SegTree

mod = 2**61 + 1
base = 136
e = (0, 0)
def op(x, y):
    if x == e:
        return y
    elif y == e:
        return x
    return (x[0] * pow(base, y[1], mod) + y[0]) % mod, x[1]+y[1]

S = "abcdedcba"
RH = SegTree(op, e, [(ord(c), 1) for c in S])