"""
行列のK乗をmodで求める
"""
def matrix_power(matrix, K, mod=998244353):
    def mul(M, N):
        n1 = len(M)
        n2 = len(M[0])
        n3 = len(N[0])
        L = [[0] * n3 for _ in range(n1)]
        for i in range(n1):
            for j in range(n3):
                for k in range(n2):
                    L[i][j] = (L[i][j] + M[i][k] * N[k][j]) % mod
        return L

    bits = K.bit_length()

    dp = [None] * (bits+1)
    dp[0] = matrix
    for i in range(1, bits+1):
        nex = mul(dp[i-1], dp[i-1])
        dp[i] = nex

    s = [[0] * len(matrix) for _ in range(len(matrix))]
    for i in range(len(matrix)):
        s[i][i] = 1
    for bit in range(bits+1):
        if K&(1<<bit):
            s = mul(dp[bit], s)

    return s