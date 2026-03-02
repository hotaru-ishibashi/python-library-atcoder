
inf = 10**9
def levenshtein(S, T):
    N = len(S); M = len(T)

    dp = [[inf] * (M+1) for _ in range(N+1)]
    for i in range(N+1):
        dp[i][0] = i
    for j in range(M+1):
        dp[0][j] = j
    # print(dp)

    for i in range(1, N+1):
        for j in range(1, M+1):
            dp[i][j] = min(
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
                dp[i-1][j-1] + (1 if S[i-1] != T[j-1] else 0),
            )
    return dp


res = levenshtein("jellyfish", "smellyfish")
print(res)