from math import comb

def catalan(n):
    return comb(2*n, n) // (n+1)


def catalan_table(N):
    dp = [0] * (N+1)
    dp[0] = 1

    for n in range(1, N+1):
        res = 0
        for i in range(n):
            res += dp[i]*dp[n-1-i]

        dp[n] = res

    return dp