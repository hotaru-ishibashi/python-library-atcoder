"""
Docstring for tsp

G: グラフ(隣接行列)
S: 始点の集合
"""
def tsp(G, S=[0]):
    V = len(G)
    dp = [[float('inf')]*V for _ in range(2**V)] 
    for s in S:
        dp[1<<s][s] = 0 
    for bit in range(2**V): 
        for u in range(V):
            if bit & (1<<u) == 0:
                continue
            for v in range(V):
                nbit = bit | 1 << v
                dp[nbit][v] = min(dp[nbit][v], dp[bit][u] + G[u][v])
    return dp