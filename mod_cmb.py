class Modcomb:
    def __init__(self, nmax, mod=998244353):
        self.cmb_memo = [1]
        self.nmax = nmax
        self.mod = mod
        for i in range(1, nmax+1):
            self.cmb_memo.append(self.cmb_memo[-1] * i % self.mod)
    def comb(self, n, k):
        if k > n:
            return 0
        if n > self.nmax or k > self.nmax:
            raise ValueError("over maximum n/k")
        return self.cmb_memo[n] * pow(self.cmb_memo[n-k], -1, self.mod) * pow(self.cmb_memo[k], -1, self.mod) % self.mod