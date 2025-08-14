

def detect_cycles(G):
    N = len(G)

    cycles = []
    dest_cycle = [-1] * N
    def dfs(v, hist, hset):
        nv = G[v]
        hist.append(v)
        hset.add(v)

        if nv in hset:
            cycle = []
            cycle_end = False
            cycle_idx = len(cycles)
            while len(hist):
                t = hist.pop()
                if not cycle_end:
                    cycle.append(t)
                dest_cycle[t] = cycle_idx
                if t == nv:
                    cycle_end = True
            cycle.reverse()
            return cycle
        
        if dest_cycle[nv] != -1:
            cycle_idx = dest_cycle[nv]
            while len(hist):
                t = hist.pop()
                dest_cycle[t] = cycle_idx
            return []
        return dfs(nv, hist, hset)
    
    for i in range(N):
        if dest_cycle[i] == -1:
            res = dfs(i, [], set())
            if len(res):
                cycles.append(res)

    return cycles, dest_cycle

if __name__ == "__main__":
    N, K = map(int, input().split())
    G = [None] * N
    P = list(map(int, input().split()))
    for i in range(N):
        G[i] = P[i]-1

    print(detect_cycles(G))