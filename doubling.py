class Doubling:
    digit = 60
    dp = None

    """
    A: 遷移先(zero_indexed)
    """
    def __init__(self, A, digit=None):
        if digit is not None:
            self.digit = digit
        N = len(A)

        dp = [[None] * N for _ in range(self.digit+1)]
        dp[0] = A

        for i in range(1, self.digit+1):
            for j in range(N):
                dp[i][j] = dp[i-1][dp[i-1][j]]
        self.dp = dp

    """
    n: 遷移前のインデックス
    K: 遷移回数
    """
    def query(self, n, K):
        if K > (1 << self.digit):
            raise ValueError("too large K")
        
        for bit in range(self.digit):
            if K & (1<<bit):
                n = self.dp[bit][n]

        return n