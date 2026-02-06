from bisect import bisect
from heapq import merge

# -----------for codon-------------------
# @extend
# class int:
#     def bit_length(self): 
#         return 64 - abs(self).__ctlz__()
#     def bit_count(self):
#         return abs(self).__ctpop__()
class MergeSortTree:
    data = []
    csum = []
    _n = 0

    def __init__(self, A):
        N = len(A)
        self._n = 2**(N-1).bit_length()
        self.data = [None]*(2*self._n)
        self.csum = [[0] for _ in range(2*self._n)]

        for i, a in enumerate(A):
            self.data[self._n-1+i] = [a]
            self.csum[self._n-1+i].append(a)
        for i in range(N, self._n):
            self.data[self._n-1+i] = []
        for i in range(self._n-2, -1, -1):
            self.data[i] = list(merge(self.data[2*i+1], self.data[2*i+2]))
            for d in self.data[i]:
                self.csum[i].append(self.csum[i][-1]+d)

    # count elements A_i s.t. A_i < k for i in [l, r)
    def range_freq_lt_k(self, l, r, k):
        L = l + self._n; R = r + self._n
        f = 0
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                idx = bisect(self.data[R-1], k-1)
                f += idx
                s += self.csum[R-1][idx]
            if L & 1:
                idx = bisect(self.data[L-1], k-1)
                f += idx
                s += self.csum[L-1][idx]
                L += 1
            L >>= 1; R >>= 1
        return f, s

    # count elements A_i s.t. a <= A_i < b for i in [l, r)
    def range_freq_a_to_b(self, l, r, a, b):
        L = l + self._n; R = r + self._n
        f = 0
        s = 0
        while L < R:
            if R & 1:
                R -= 1
                ri, li = bisect(self.data[R-1], b-1), bisect(self.data[R-1], a-1)
                f += ri - li
                s += self.csum[R-1][ri] - self.csum[R-1][li]
            if L & 1:
                ri, li = bisect(self.data[L-1], b-1), bisect(self.data[L-1], a-1)
                f += ri - li
                s += self.csum[L-1][ri] - self.csum[L-1][li]
                L += 1
            L >>= 1; R >>= 1
        return f, s


A = [6, 1, 4, 5, 3, 2]
mst = MergeSortTree(A)
print(mst.range_freq_lt_k(1, 5, 5))
# => "1"
print(mst.range_freq_a_to_b(0, 6, 2, 5))
# => "1"