from typing import Callable, List, Tuple


class LazySegTree[S, F]:
    _op: Callable[[S, S], S]
    _e: S
    _mapping: Callable[[F, S], S]
    _composition: Callable[[F, F], F]
    _id: F
    _n: int
    _log: int
    _size: int
    _d: List[S]
    _lz: List[F]

    def __init__(
        self,
        op: Callable[[S, S], S],
        e: S,
        mapping: Callable[[F, S], S],
        composition: Callable[[F, F], F],
        id_: F,
        v: List[S],
    ) -> None:
        self._op = op
        self._e = e
        self._mapping = mapping
        self._composition = composition
        self._id = id_

        self._n = len(v)
        n0 = self._n
        size = 1
        log = 0
        while size < n0:
            size <<= 1
            log += 1
        self._log = log
        self._size = size
        self._d = [e] * (2 * self._size)
        self._d[self._size:self._size + self._n] = v
        for i in range(self._size - 1, 0, -1):
            self._update(i)
        self._lz = [id_] * self._size

    def _update(self, k: int) -> None:
        self._d[k] = self._op(self._d[2 * k], self._d[2 * k + 1])

    def _all_apply(self, k: int, f: F) -> None:
        self._d[k] = self._mapping(f, self._d[k])
        if k < self._size:
            self._lz[k] = self._composition(f, self._lz[k])

    def _push(self, k: int) -> None:
        f = self._lz[k]
        if f != self._id:
            self._all_apply(2 * k, f)
            self._all_apply(2 * k + 1, f)
            self._lz[k] = self._id

    def set(self, p: int, x: S) -> None:
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        self._d[p] = x
        for i in range(1, self._log + 1):
            self._update(p >> i)

    def get(self, p: int) -> S:
        p += self._size
        for i in range(self._log, 0, -1):
            self._push(p >> i)
        return self._d[p]

    def prod(self, l: int, r: int) -> S:
        if l == r:
            return self._e
        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if (l >> i << i) != l:
                self._push(l >> i)
            if (r >> i << i) != r:
                self._push((r - 1) >> i)
        sml = self._e
        smr = self._e
        while l < r:
            if l & 1:
                sml = self._op(sml, self._d[l])
                l += 1
            if r & 1:
                r -= 1
                smr = self._op(self._d[r], smr)
            l >>= 1
            r >>= 1
        return self._op(sml, smr)

    def all_prod(self) -> S:
        return self._d[1]

    def apply(self, l: int, r: int, f: F) -> None:
        if l == r:
            return
        l += self._size
        r += self._size
        for i in range(self._log, 0, -1):
            if (l >> i << i) != l:
                self._push(l >> i)
            if (r >> i << i) != r:
                self._push((r - 1) >> i)
        l2, r2 = l, r
        while l < r:
            if l & 1:
                self._all_apply(l, f)
                l += 1
            if r & 1:
                r -= 1
                self._all_apply(r, f)
            l >>= 1
            r >>= 1
        l, r = l2, r2
        for i in range(1, self._log + 1):
            if (l >> i << i) != l:
                self._update(l >> i)
            if (r >> i << i) != r:
                self._update((r - 1) >> i)

    def max_right(self, l: int, g: Callable[[S], bool]) -> int:
        if l == self._n:
            return self._n
        l += self._size
        for i in range(self._log, 0, -1):
            self._push(l >> i)
        sm = self._e
        while True:
            while l % 2 == 0:
                l >>= 1
            if not g(self._op(sm, self._d[l])):
                while l < self._size:
                    self._push(l)
                    l <<= 1
                    if g(self._op(sm, self._d[l])):
                        sm = self._op(sm, self._d[l])
                        l += 1
                return l - self._size
            sm = self._op(sm, self._d[l])
            l += 1
            if (l & -l) == l:
                break
        return self._n

    def min_left(self, r: int, g: Callable[[S], bool]) -> int:
        if r == 0:
            return 0
        r += self._size
        for i in range(self._log, 0, -1):
            self._push((r - 1) >> i)
        sm = self._e
        while True:
            r -= 1
            while r > 1 and r % 2:
                r >>= 1
            if not g(self._op(self._d[r], sm)):
                while r < self._size:
                    self._push(r)
                    r = r * 2 + 1
                    if g(self._op(self._d[r], sm)):
                        sm = self._op(self._d[r], sm)
                        r -= 1
                return r + 1 - self._size
            sm = self._op(self._d[r], sm)
            if (r & -r) == r:
                break
        return 0

mod = 998244353


N, M = list(map(int, input().split()))
A = list(map(int, input().split()))
ID = 10**18
tree = LazySegTree[Tuple[int, int], int](
    lambda d1, d2: ((d1[0]+d2[0])%mod, d1[1]+d2[1]), 
    (0, 0), 
    lambda l, d: d if l == ID else ((l*d[1])%mod, d[1]), 
    lambda l1, l2: l2 if l1 == ID else l1,
    ID,
    [(e, 1) for e in A]
)

for _ in range(M):
    L, R = list(map(int, input().split()))
    L-=1; R-=1
    
    s = tree.prod(L, R+1)[0]
    denom = pow(R-L+1, mod-2, mod)
    a = (s*denom)%mod
    tree.apply(L, R+1, a%mod)
    
for p in range(N):
    print(tree.get(p)[0], end=" ")
    