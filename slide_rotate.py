from collections import deque
from atcoder.fenwicktree import FenwickTree

def slide_rotate(A, K):
    N = len(A)
    ma = max(A)
    K_tree = FenwickTree(ma+1)
    seg = deque()

    res = []

    rotate_k = 0
    for i in range(K):
        a = A[i]
        seg.append(a)
        rotate_k += K_tree.sum(a+1, ma+1)
        K_tree.add(a, 1)
    res.append(rotate_k)

    for k_l in range(N-K):
        next_a = A[K+k_l]
        prev_a = seg.popleft()

        rotate_k -= K_tree.sum(0, prev_a)
        K_tree.add(prev_a, -1)
        K_tree.add(next_a, 1)
        rotate_k += K_tree.sum(next_a+1, N+1)
        seg.append(next_a)

        res.append(rotate_k)

    return res

    