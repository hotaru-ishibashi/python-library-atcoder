from operator import itemgetter

"""_summary_
Mo's algorithm
区間和クエリのサンプル

1. 状態を設計する
対象区間が[l, r)の時に、クエリに回答するために必要なstateを設計する
_init_states内に実装

2. 差分更新処理を実装する
_addと_delを実装する
self.ls[i]を追加/削除する場合にstateがどう変わるかを考える
(できなくね?となったらMoではないかも)

隣接項が必要な場合や、左右どちらに追加するかが知りたい場合は引数のdirection(左: 0, 右: 1)を参照する

3. 回答算出処理を実装する
stateから実際のクエリの回答を返す関数を実装する
直接答えをstateで管理するならreturn state.ansでOK
"""

class Mo:
    # ls:　走査対象の配列
    def __init__(self, ls):
        from math import sqrt, ceil
        self.ls = ls
        self.n = len(ls)
        self.b = ceil(sqrt(self.n))  # bukectのサイズ及び個数

    def _init_states(self):
        ########################################
        # 配列の[l, r)が範囲になっているときのステータス  ココには初期状態(空配列)の場合のステータスを書く
        self.ans = 0
        
        # 頻度列を持ちがち
        # self.cnt = defaultdict(lambda: 0)
        ########################################
        
        # 汎用ステータス。差分更新時の実装は不要
        self.num = 0; self.l = 0; self.r = 0
        # queryを格納する用
        self.bucket = [list() for _ in range((self.b + 1))]

    # 区間を伸ばす self.ls[i]を追加   direction: 左に追加するか右に追加するか
    def _add(self, i, direction):
        self.ans += self.ls[i]
        
    # 区間を縮める self.ls[i]を削除   direction: 左に追加するか右に追加するか
    def _delete(self, i, direction):
        self.ans -= self.ls[i]
        
    # 現在の状態から、クエリの答えの値を算出する
    def _answer(self):
        return self.ans

    def _one_process(self, l, r):
        # クエリ[l,r)に対してstatesを更新する
        for i in range(self.r, r): self._add(i, 1); self.num += 1
        for i in range(self.r - 1, r - 1, -1): self._delete(i, 1); self.num -= 1
        for i in range(self.l, l): self._delete(i, 0); self.num -= 1
        for i in range(self.l - 1, l - 1, -1): self._add(i, 0); self.num += 1
        self.l = l
        self.r = r

    def process(self, queries):
        self._init_states()
        # クエリをいい感じに平方分割　触らない
        for i, (l, r) in enumerate(queries): self.bucket[l // self.b].append((l, r, i))
        for i in range(len(self.bucket)): self.bucket[i].sort(key=itemgetter(1))

        ret = [-1] * len(queries)
        for b in self.bucket:
            for l, r, i in b:  # クエリに答えていく
                self._one_process(l, r)
                ret[i] = self._answer()
        return ret
    
    
A = [1, 2, 3, 4, 5]
query = [[0, 3], [2, 4]]
mo = Mo(A)
print(mo.process(query))
