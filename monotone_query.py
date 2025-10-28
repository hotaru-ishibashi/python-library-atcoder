from atcoder.fenwicktree import FenwickTree
from typing import Literal

class MonotoneQueryTree:
    def __init__(self, A, type: Literal["increasing","decreasing"]="increasing", strict: bool=False):
        """
        A: 元配列
        type: "increasing" または "decreasing"
        strict: True → 狭義, False → 広義
        """
        self.N = len(A)
        self.A = A[:]
        self.type = type
        self.strict = strict

        # 比較関数を生成
        self.cmp = self._make_cmp(type, strict)

        # BITに非単調箇所を登録
        self.bit = FenwickTree(max(1, self.N-1))
        for i in range(self.N - 1):
            if self.cmp(self.A[i], self.A[i+1]):
                self.bit.add(i, 1)

    def _make_cmp(self, type, strict):
        if type == "increasing":
            if strict:
                return lambda a,b: a >= b  # 狭義増加に違反する箇所
            else:
                return lambda a,b: a > b   # 広義増加に違反する箇所
        elif type == "decreasing":
            if strict:
                return lambda a,b: a <= b  # 狭義減少に違反する箇所
            else:
                return lambda a,b: a < b   # 広義減少に違反する箇所
        else:
            raise ValueError("type must be 'increasing' or 'decreasing'")

    def get(self, i):
        return self.A[i]

    def update(self, i, x):
        N = self.N
        self.A[i] = x

        # 左側境界
        if i > 0:
            self.bit.add(i-1, -self.bit.sum(i-1,i))
            if self.cmp(self.A[i-1], self.A[i]):
                self.bit.add(i-1, 1)

        # 右側境界
        if i < N-1:
            self.bit.add(i, -self.bit.sum(i,i+1))
            if self.cmp(self.A[i], self.A[i+1]):
                self.bit.add(i, 1)

    def query(self, l, r):
        """区間 [l,r) が指定の単調かどうか"""
        if r-l <= 1:
            return True
        return self.bit.sum(l, r-1) == 0
