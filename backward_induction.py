from collections import deque

"""
G: 有向グラフ
"""
def backward_induction(G):
    WIN = 1
    LOSE = 0
    TBD = -1
    N = len(G)
    deg = [0] * N
    Ginv = [[] for _ in range(N)]
    dp = [-1] * N
    queue = deque()

    for v in range(N):
        deg[v] = len(G[v])
        if deg[v] == 0:
            dp[v] = LOSE
            queue.append(v)

        for nv in G[v]:
            Ginv[nv].append(v)
    
    while len(queue):
        cv = queue.popleft()

        # 遷移元を走査
        for nv in Ginv[cv]:
            # 確定済み頂点への再訪はスルー
            if dp[nv] != TBD:
                continue
            deg[nv] -= 1
            if dp[cv] == LOSE:
                dp[nv] = WIN
                queue.append(nv)
            elif dp[cv] == WIN and deg[nv] == 0:
                dp[nv] = LOSE
                queue.append(nv)

    return dp