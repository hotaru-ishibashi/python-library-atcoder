from operator import itemgetter
class Mo:
    def __init__(self, ls):
        from math import sqrt, ceil
        self.ls = ls
        self.n = len(ls)
        self.b = ceil(sqrt(self.n))  # bukectのサイズ及び個数

    def _init_states(self):
        ########################################
        # クエリに対する答え
        self.ans = 0
        self.num = 0
        self.cnt = defaultdict(lambda: 0)
        ########################################

        # [l,r)の半開区間で考える
        self.l = 0
        self.r = 0

        # queryを格納する用
        self.bucket = [list() for _ in range((self.b + 1))]

    # 区間を伸ばす self.ls[i]を追加
    def _add(self, i):
        self.cnt[self.ls[i]] += 1
        self.num += 1
        
        # クエリの答えの差分を更新
        # self.ans = 
        
    # 区間を縮める self.ls[i]を削除
    def _delete(self, i):
        self.cnt[self.ls[i]] -= 1
        self.num -= 1 
        
        # クエリの答えの差分を更新
        # self.ans = 

    def _one_process(self, l, r):
        # クエリ[l,r)に対してstatesを更新する
        for i in range(self.r, r):  # rまで伸長
            self._add(i)
        for i in range(self.r - 1, r - 1, -1):  # rまで短縮
            self._delete(i)
        for i in range(self.l, l):  # lまで短縮
            self._delete(i)
        for i in range(self.l - 1, l - 1, -1):  # lまで伸長
            self._add(i)

        self.l = l
        self.r = r

    def process(self, queries):
        self._init_states()

        for i, (l, r) in enumerate(queries):  # queryをbucketに格納
            self.bucket[l // self.b].append((l, r, i))

        for i in range(len(self.bucket)):
            self.bucket[i].sort(key=itemgetter(1))

        ret = [-1] * len(queries)
        for b in self.bucket:
            for l, r, i in b:  # クエリに答えていく
                self._one_process(l, r)
                ########################################
                # クエリに答える作業をここで書く
                ret[i] = self.ans
                ########################################
        return ret