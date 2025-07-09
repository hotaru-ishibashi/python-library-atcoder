from collections import deque

def bfs(G, N, s):
    que = deque([s])
    dist = [-1] * N
    dist[s] = 0

    while len(que):
        cv = que.popleft()
        cd = dist[cv]

        for nv in G[cv]:
            if dist[nv] != -1:
                continue
            dist[nv] = cd + 1
            que.append(nv)
            
    return dist