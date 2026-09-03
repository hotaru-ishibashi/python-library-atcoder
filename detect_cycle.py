def detect_cycle(G, s=0, directed=False):
    n = len(G)

    vis = [False] * n
    finished = [False] * n
    parent = [-1] * n
    hist = []
    hist_pos = [-1] * n

    def dfs(u):
        vis[u] = True
        hist_pos[u] = len(hist)
        hist.append(u)

        for v in G[u]:
            if not directed and v == parent[u]:
                continue
            if not vis[v]:
                parent[v] = u
                cycle = dfs(v)
                if cycle is not None:
                    return cycle
            elif not finished[v]:
                # サイクル発見
                # hist = [s, ..., v, .............., u]
                #                | ここ(v-u)がサイクル | 
                # cycle_length = len(hist) - hist_pos[v] 
                return hist[hist_pos[v]:]

        hist.pop()
        hist_pos[u] = -1
        finished[u] = True
        return None

    return dfs(s)
