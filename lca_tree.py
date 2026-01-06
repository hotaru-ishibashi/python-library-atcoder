class LCATree:
    def __init__(self, n: int):
        self.n = n
        self.G = [list[int]() for _ in range(n)]
        self.LOG = 0
        while (1 << self.LOG) <= n:
            self.LOG += 1

        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.depth = [-1] * n

    def add_edge(self, u: int, v: int):
        self.G[u].append(v)
        self.G[v].append(u)

    def build(self, root: int = 0):
        # 非再帰 DFS
        stack = [root]
        self.depth[root] = 0
        self.parent[0][root] = -1

        while stack:
            v = stack.pop()
            for to in self.G[v]:
                if self.depth[to] == -1:
                    self.depth[to] = self.depth[v] + 1
                    self.parent[0][to] = v
                    stack.append(to)

        # doubling
        for k in range(self.LOG - 1):
            for v in range(self.n):
                p = self.parent[k][v]
                self.parent[k + 1][v] = -1 if p == -1 else self.parent[k][p]

    # 頂点uのk代前の祖先頂点 O(logN)
    def kth_ancestor(self, u: int, k: int) -> int:
        cur = u
        i = 0
        while k and cur != -1:
            if k & 1:
                cur = self.parent[i][cur]
            k >>= 1
            i += 1
        return cur

    def lca(self, u: int, v: int) -> int:
        if self.depth[u] < self.depth[v]:
            u, v = v, u

        diff = self.depth[u] - self.depth[v]
        u = self.level_ancestor(u, diff)

        if u == v:
            return u

        for k in range(self.LOG - 1, -1, -1):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]

        return self.parent[0][u]

    # u-v間の距離 O(logN)
    def dist(self, u: int, v: int) -> int:
        w = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[w]

    # u-vパス上に頂点wが存在するか O(logN)
    def in_path(self, u: int, v: int, w: int) -> bool:
        return self.dist(u, w) + self.dist(w, v) == self.dist(u, v)
    
    # u-vパス上で、uから見た隣接頂点 O(logN)
    def nxt(self, u: int, v: int) -> int:
        if u == v: return -1
        w = self.lca(u, v)
        # v が u の親側にある
        if w != u:
            return self.parent[0][u]
        # v が u の部分木側にある
        # v を depth[u] + 1 まで持ち上げる
        return self.level_ancestor(v, self.depth[v] - self.depth[u] - 1)
    

N = int(input())
G = [[] for _ in range(N)]
lca = LCATree(N)
for _ in range(N-1):
    u, v = list(map(int, input().split()))
    G[u].append(v)
    G[v].append(u)
    lca.add_edge(u, v)
# 根を指定
lca.build(0)