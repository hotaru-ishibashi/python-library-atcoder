
""" @@@ EDIT @@@ """
nmax = 3010
mod = 998244353
""" @@@@@@@@@@@@ """
fac = [0] * (nmax+1)
ifac = [0] * (nmax+1)
fac[0] = ifac[0] = 1
for i in range(1, nmax+1): fac[i] = fac[i-1]*i%mod
ifac[nmax] = pow(fac[nmax], mod-2, mod)
for i in range(nmax-1, 0, -1): ifac[i] = ifac[i+1]*(i+1)%mod
def C(n, k):
    if k > n: return 0
    return fac[n] * ifac[n-k] * ifac[k] % mod
def H(n, k):
    if k > n: return 0
    return C(n+k-1, k)

class CompositeModComb:
    def __init__(self, nmax, mod):
        dp = [[0] * (nmax + 1) for _ in range(nmax + 1)]
        dp[1][1] = 1
        for i in range(nmax + 1):
            dp[i][0] = 1
        for n in range(2, nmax + 1):
            for r in range(1, n+1):
                dp[n][r] = dp[n-1][r-1] + dp[n-1][r]
                dp[n][r] %= mod

        self.memo = dp

    def comb(self, n, r):
        return self.memo[n][r]