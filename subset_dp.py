



"""
N個の物を任意の個数のグループに分ける
N: 要素数
op: dpを更新する際の演算
e: dpの初期値
eval: 集合s(bit)1つのグループの際の評価値
"""
def subset_dp(N, op, e, eval, merge=lambda x, y:x+y):
    dp = [e for _ in range(1<<N)]
    for s in range(1, 1<<N):
        dp[s] = eval(s)

        t = s&(s-1)
        # sをss/tに分割
        while t:
            ss = s-t
            dp[s] = op(dp[s], merge(dp[ss],dp[t]))
            t = s&(t-1)
    return dp


# def eval(s):
#     res = 0
#     for i in range(N):
#         if s&1<<i:
#             res +=A[i]
#     return res
# dp = subset_dp(N, min, 10**18, eval)
# dp[(1<<N)-1]

""" @@@codon用@@@ """
# @extend
# class int:
#     def bit_length(self): 
#         return 64 - abs(self).__ctlz__()
#     def bit_count(self):
#         return abs(self).__ctpop__()

"""
N個の物をD個以下のグループに分ける
N: 要素数
D: グループ数の上限
op: dpを更新する際の演算
e: dpの初期値
eval: 集合s(bit)1つのグループの際の評価値
"""
def subset_dp_d(N, D, op, e, eval, merge=lambda x, y:x+y):
    dp = [[e] * (D+1) for _ in range(1<<N)]
    for s in range(1, 1<<N):
        # sを1つの集合とする場合
        dp[s][1] = eval(s)

        for d in range(2, min(s.bit_count(), D)+1):
            t = s&(s-1)
            # sをss/tに分割
            # ssを1つ、tをd-1個に分割した結果でdp[s][d]を更新
            while t:
                ss = s-t
                dp[s][d] = op(dp[s][d], merge(dp[ss][1],dp[t][d-1]))
                t = s&(t-1)
    return dp

# def eval(s):
#     res = 0
#     for i in range(N):
#         if s&1<<i:
#             res +=A[i]
#     return res
# dp = subset_dp(N, D, min, 10**18, eval)
# min(dp[(1<<N)-1])