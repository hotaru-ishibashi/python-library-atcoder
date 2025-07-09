from heapq import heappush, heappop

def dijkstra(G, N, s):
    que = [(0, s)]
    dist = [float("inf")] * N
    dist[s] = 0

    while len(que):
        cd, cv = heappop(que)
        if cd != dist[cv]:
            continue

        for nv, cost in G[cv]:
            nd = cd + cost
            if dist[nv] <= nd:
                continue
            dist[nv] = nd
            heappush(que, (nd, nv))
            
    return dist