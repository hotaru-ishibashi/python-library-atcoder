from atcoder.lazysegtree import LazySegTree

A = [1, 3, 5, -2, -10, 100, 0]
inf = float("inf")
# range add / range sum
tree = LazySegTree(
    lambda d1, d2: (d1[0]+d2[0], d1[1]+d2[1]), 
    (0, 0), 
    lambda l, d: (d[0]+d[1]*l, d[1]), 
    lambda l1, l2: l1+l2,
    0,
    [[e, 1] for e in A]
)
# range add / range sum
tree = LazySegTree(
    lambda d1, d2: (d1[0]+d2[0], d1[1]+d2[1]), 
    (0, 0), 
    lambda l, d: (d[0]+d[1]*l, d[1]), 
    lambda l1, l2: l1+l2,
    0,
    [[e, 1] for e in A]
)
# range add / range max
tree = LazySegTree(
    max, 
    -inf, 
    lambda l, d: d + l, 
    lambda l1, l2: l1+l2,
    -inf,
    0
)
# range add / range min
tree = LazySegTree(
    min, 
    inf, 
    lambda l, d: d + l, 
    lambda l1, l2: l1+l2,
    inf,
    0
)

# range add / range sum
tree = LazySegTree(
    lambda d1, d2: (d1[0]+d2[0], d1[1]+d2[1]), 
    (0, 0), 
    lambda l, d: (d[0]+d[1]*l, d[1]), 
    lambda l1, l2: l1+l2,
    0,
    [[e, 1] for e in A]
)

ID = 8e18
# range change / range sum
tree = LazySegTree(
    lambda d1, d2: (d1[0]+d2[0], d1[1]+d2[1]), 
    (0, 0), 
    lambda l, d: d if l == ID else (l*d[1], d[1]), 
    lambda l1, l2: l2 if l1 == ID else l1,
    ID,
    [[e, 1] for e in A]
)
# range change / range max
tree = LazySegTree(
    max, 
    -inf, 
    lambda l, d: d if l == ID else l, 
    lambda l1, l2: l2 if l1 == ID else l2,
    ID,
    A
)
# range change / range min
tree = LazySegTree(
    min, 
    inf, 
    lambda l, d: d if l == ID else l, 
    lambda l1, l2: l2 if l1 == ID else l2,
    ID,
    A
)