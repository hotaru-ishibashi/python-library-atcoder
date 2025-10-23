# https://qiita.com/drken/items/a207e5ae3ea2cf17f4b

def next_i(s):
    N = len(s)
    res = [[None] * 26 for _ in range(N+1)]
    for i in range(N-1, -1, -1):
        for j in range(26):
            res[i][j] = res[i+1][j]
        res[i][ord(s[i])-97] = i
    return res


def subsequence_dp(s):
    next_memo = next_i(s)
    N = len(s)

    dp = [0] * (N+1)
    dp[0] = 1

    for i in range(N):
        # print(i, next_memo[i])
        for j in range(26):
            if next_memo[i][j] is not None:
                dp[next_memo[i][j] + 1] += dp[i]

    # print(next_memo)
    return dp

