from collections import deque


def bfs(G, s=0):
    dists = [-1] * len(G)
    que = deque([s])
    dists[s] = 0

    while len(que):
        cv = que.popleft()

        for nv in G[cv]:
            if dists[nv] != -1:
                continue
            dists[nv] = dists[cv] + 1
            que.append(nv)

    return dists



def diameter(G):
    """
    :return: U, V, Uからの距離, Vからの距離, 直径, 離心数, 中心(1or2個)
    """
    N = len(G)
    dists0 = bfs(G)
    farest, farest_dist = -1, -1
    for i, d in enumerate(dists0):
        if d > farest_dist:
            farest_dist = d
            farest = i
    
    # 端点1からの距離
    dists_f = bfs(G, farest)
    farest2, farest_dist2 = -1, -1
    for i, d in enumerate(dists_f):
        if d > farest_dist2:
            farest_dist2 = d
            farest2 = i
    dists_f2 = bfs(G, farest2)

    # 離心数
    eccentricity = [0] * N
    min_ec = N
    for i in range(N):
        ec = max(dists_f[i], dists_f2[i])
        eccentricity[i] = ec
        min_ec = min(min_ec, ec)
    centers = []
    for i in range(N):
        if min_ec == eccentricity[i]:
            centers.append(i)

    return farest, farest2, dists_f, dists_f2, farest_dist2, eccentricity, centers


def bfs_subtree(G, dists, que):    
    while len(que):
        cv = que.popleft()
        for nv in G[cv]:
            if dists.get(nv) is not None:
                continue
            dists[nv] = dists[cv] + 1
            que.append(nv)
    return dists

# 直径の端点を列挙
def enumerate_edges(G, centers, diameter):
    if len(centers) == 1:
        c = centers[0]
        res = {}
        radius = diameter // 2
        for nb in G[c]:
            que = deque([nb])
            dists = bfs_subtree(G, { c : 0, nb: 1 }, que)
            res[nb] = []
            for v in dists.keys():
                if dists[v] == radius:
                    res[nb].append(v)
    else:
        c1, c2 = centers
        res = { c1: [], c2: []}

        d1 = { c1: 0, c2: -1}
        q1 = deque([c1])
        dists1 = bfs_subtree(G, d1, q1)
        md1 = max(dists1.values())
        for v in dists1.keys():
            if dists1[v] == md1:
                res[c1].append(v)

        d2 = { c2: 0, c1: -1}
        q2 = deque([c2])
        dists2 = bfs_subtree(G, d2, q2)
        md2 = max(dists2.values())
        for v in dists2.keys():
            if dists2[v] == md2:
                res[c2].append(v)
    return res

N = int(input())
G = [[] for _ in range(N)]
for _ in range(N-1):
    u, v = map(lambda x: int(x)-1, input().split())
    G[u].append(v)
    G[v].append(u)

s, t, df1, df2, diam, eccentricity, centers = diameter(G)
# print(eccentricity, diam, centers)

res = enumerate_edges(G, centers, diam)

