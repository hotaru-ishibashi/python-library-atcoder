from bisect import bisect_left
inf = 1<<60

def LIS(A):
    N = len(A)

    dp = [inf] * (N+1)
    dp[0] = 0

    for val in A:
        update_idx = bisect_left(dp, val)
        dp[update_idx] = val

    lis = bisect_left(dp, inf) - 1

    return dp, lis

a = [2, 6, 4, 0, 16, 8, 2]
print(LIS(a))