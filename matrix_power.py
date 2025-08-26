import numpy as np
from sys import exit

# 数列aの第X項を求める
X = 100
if X == 1:
    # TODO コーナーケース
    print()
    exit()

# TODO [a2, a1]
s = np.array([])
# TODO 遷移行列
matrix = np.array([[], []])
bits = 40

dp = [None] * (bits+1)
dp[0] = matrix
for i in range(1, bits+1):
    nex = np.matmul(dp[i-1], dp[i-1])
    # TODO 必要に応じてmodとったり
    dp[i] = nex
    
for bit in range(bits+1):
    if (X-2)&(1<<bit):
        s = np.matmul(dp[bit], s)
        # TODO 必要に応じてmodとったり

print(s[0])