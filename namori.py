class Namori:
    def __init__(self, N):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.degs = [0] * N

    def add_edge(self, u, v):
        self.G[u].append(v)
        self.G[v].append(u)
        self.degs[u] += 1
        self.degs[v] += 1

    def detect_cycle(self):
        cycle = [True] * self.N

        deg1_v = []
        for i in range(self.N):
            if self.degs[i] == 1:
                deg1_v.append(i)
                cycle[i] = False

        while len(deg1_v):
            v = deg1_v.pop()
            for nv in self.G[v]:
                if not cycle[nv]:
                    continue
                self.degs[nv] -= 1
                if self.degs[nv] == 1:
                    deg1_v.append(nv)
                    cycle[nv] = False
        
        roots = [-1] * self.N
        for root in range(self.N):
            if not cycle[root]:
                continue
            que = [root]

            while len(que):
                cv = que.pop()

                for nv in self.G[cv]:
                    if cycle[nv] or roots[nv] != -1:
                        continue
                    roots[nv] = root
                    que.append(nv)
                    
        return roots


N = int(input())
namori = Namori(N)
for i in range(N):
    u, v = map(lambda x:int(x)-1, input().split())
    namori.add_edge(u, v)
roots = namori.detect_cycle()