from bisect import bisect_left
inf = 1<<60

def LIS(A):
    N = len(A)

    dp = [inf] * (N+1)
    dp[0] = -inf
    # A[i]が増加列の何番目か
    idx_memo = [None] * N

    for i, val in enumerate(A):
        update_idx = bisect_left(dp, val)
        dp[update_idx] = val
        idx_memo[i] = update_idx

    lis_len = bisect_left(dp, inf) - 1
    return dp, lis_len, idx_memo

def reconstruct(A, lis_len, idx_memo):
    N = len(A)

    t_idx = lis_len
    hist = []
    for i in range(N-1, -1, -1):
        if idx_memo[i] == t_idx:
            hist.append((A[i], i))
            t_idx -= 1

    hist.reverse()
    return hist


a = [5, 6, 7, 1, 2, 3, 4]
dp, lis_len, idx_memo = LIS(a)
lis = reconstruct(a, lis_len, idx_memo)

print(lis)