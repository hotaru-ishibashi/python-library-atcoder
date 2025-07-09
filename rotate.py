from atcoder.fenwicktree import FenwickTree
from bisect import bisect_left

def rotate(A):
    N = len(A)
    As = sorted(A)
    comp = []
    for a in A:
        idx = bisect_left(As, a)
        comp.append(idx)

    # print(comp)
    tree = FenwickTree(N)

    # R = [0] * 10
    res = [0] * 10
    for i in range(10):
        a = comp[i]

        tree.add(a, 1)
        # print(tree.sum(a+1, N))
        res[i] = tree.sum(a+1, N)
    return res


a = [0, 3, 1, 9, 5, 6, 3, 2000000000000000000000000000, 11, 2]
print(rotate(a))