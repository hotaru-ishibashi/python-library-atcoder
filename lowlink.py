from sys import setrecursionlimit
setrecursionlimit(10**6)

def lowlink(N, G):
    ords = [-1] * N
    lows = [N+1] * N

    def dfs(v, order):
        ords[v] = order
        low = order

        inc = 1
        for nv in G[v]:
            if ords[nv] == -1:
                dfs(nv, order+inc)
                inc += 1
            nlow = lows[nv]
            if nlow > order:
                lows[nv] = order
            low = min(low, nlow)

        lows[v] = low
        return low
    
    dfs(0, 0)

    return ords, lows

N = 3
G = [[1, 2], [0], []]

lowlink(N, G)