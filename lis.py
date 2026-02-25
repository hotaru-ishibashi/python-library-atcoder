from bisect import bisect_left
inf = 1<<60

def LIS(A):
    N = len(A)
    dp = [] 
    # A[i]が増加列の何番目か
    idx_memo = [None] * N

    for i, val in enumerate(A):
        update_idx = bisect_left(dp, val)
        idx_memo[i] = update_idx

        if update_idx == len(dp):
            dp.append(val)
        else:
            dp[update_idx] = val

    lis_len = len(dp)

    cand = [[] for _ in range(lis_len)]
    for i in range(N-1, -1, -1):
        if (idx_memo[i] == lis_len - 1) or (len(cand[idx_memo[i]+1]) != 0 and A[i] < A[cand[idx_memo[i]+1][-1]]):
            cand[idx_memo[i]].append(i)
        else:
            idx_memo[i] = -1

    return dp, lis_len, idx_memo, cand


# https://miscalc.hatenablog.com/entry/2024/07/25/212618
a = [2, 7, 1, 8, 2, 8, 1, 8]
dp, lis_len, idx_memo, cand = LIS(a)
# // idx_memo[i] := A の i 番目が LIS に使われ得るなら LIS の何番目か、使われ得ないなら -1
# // cand[j] := LIS の j 番目になりうる A の要素の添字の配列 (添字の昇順、値の降順)
# // cand[j].front() たちをとってきたもの: 添字の辞書順最小、値の辞書順最大の LIS
# // cand[j].back()  たちをとってきたもの: 添字の辞書順最大、値の辞書順最小の LIS
# print(dp, lis_len, idx_memo, cand)
