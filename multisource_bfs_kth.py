from collections import deque

def multisource_bfs(G, sources, k=1):
    N = len(G)
    que = deque([[s, s, 0] for s in sources])
    dist = [[[-1, -1] for _ in range(k)] for _ in range(N)]
    for v in sources:
        dist[v][0] = [0, v]
        
    while len(que):
        cv, source, cd = que.popleft()
        nd = cd + 1
        for nv in G[cv]:
            dists = dist[nv]
            #　k番目まで確定済み
            if dists[-1][0] != -1:
                continue
            visited = False
            for i, (d, s) in enumerate(dists):
                if d != -1:
                    # 確定済みかつ、同じsourceがある場合は終わり
                    if s == source:
                        visited = True
                        break
                    continue
                dist[nv][i] = [nd, source]
                break
                
            if not visited:
                que.append([nv, source, nd])
                
    return dist
