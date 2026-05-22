
class HLD:
    """
    Heavy-Light Decomposition
    (AtCoder 解説記事準拠)

    id[v]:
        頂点 v の DFS順番号

    vertex[i]:
        DFS順 i 番目の頂点番号

    subtree[v]:
        部分木サイズ

    head[v]:
        v が属する heavy path の先頭
    """

    def __init__(self, n, graph, root=0):

        self.n = n
        self.g = graph
        self.root = root

        self.parent = [-1] * n
        self.depth = [0] * n

        self.subtree = [1] * n
        self.heavy = [-1] * n

        self.head = [0] * n

        # v -> DFS order
        self.id = [0] * n

        # DFS order -> v
        self.vertex = [0] * n

        self._dfs_size(root)
        self._dfs_hld(root, root)

    def _dfs_size(self, root):
        """
        非再帰 DFS

        - parent
        - depth
        - subtree
        - heavy
        """

        order = []

        stack = [root]

        self.parent[root] = -1
        self.depth[root] = 0

        # DFS order
        while stack:

            v = stack.pop()

            order.append(v)

            for to in self.g[v]:

                if to == self.parent[v]:
                    continue

                self.parent[to] = v
                self.depth[to] = self.depth[v] + 1

                stack.append(to)

        # post-order
        for v in reversed(order):

            max_size = 0

            for to in self.g[v]:

                if to == self.parent[v]:
                    continue

                self.subtree[v] += self.subtree[to]

                if self.subtree[to] > max_size:
                    max_size = self.subtree[to]
                    self.heavy[v] = to

    def _dfs_hld(self, root, h):
        """
        非再帰 HLD DFS

        - id
        - vertex
        - head
        """

        stack = [(root, h)]

        cur = 0

        while stack:

            v, h = stack.pop()

            # heavy path を一直線に処理
            while v != -1:

                self.head[v] = h

                self.id[v] = cur
                self.vertex[cur] = v

                cur += 1

                # light edge は後で処理
                for to in reversed(self.g[v]):

                    if to == self.parent[v]:
                        continue

                    if to == self.heavy[v]:
                        continue

                    stack.append((to, to))

                v = self.heavy[v]

    def lca(self, u, v):
        """
        Lowest Common Ancestor
        """

        while self.head[u] != self.head[v]:

            if self.depth[self.head[u]] > self.depth[self.head[v]]:
                u = self.parent[self.head[u]]
            else:
                v = self.parent[self.head[v]]

        if self.depth[u] < self.depth[v]:
            return u

        return v

    def dist(self, u, v):
        """
        辺数距離
        """

        l = self.lca(u, v)

        return (
            self.depth[u]
            + self.depth[v]
            - 2 * self.depth[l]
        )

    def subtree_range(self, v):
        """
        部分木区間 [l, r)
        """

        l = self.id[v]
        r = l + self.subtree[v]

        return l, r

    def path_ranges(self, u, v, edge=False):
        """
        u-v path を O(logN) 個の区間へ分解

        return:
            list[(l, r)]

        各区間は [l, r)

        edge=False:
            頂点クエリ

        edge=True:
            辺クエリ
        """

        left = []
        right = []

        while self.head[u] != self.head[v]:

            if self.depth[self.head[u]] > self.depth[self.head[v]]:

                left.append((
                    self.id[self.head[u]],
                    self.id[u] + 1,
                ))

                u = self.parent[self.head[u]]

            else:

                right.append((
                    self.id[self.head[v]],
                    self.id[v] + 1,
                ))

                v = self.parent[self.head[v]]

        l = min(self.id[u], self.id[v])
        r = max(self.id[u], self.id[v]) + 1

        if edge:
            l += 1

        left.append((l, r))

        return left + right[::-1]

    def jump(self, u, v, k):
        """
        path(u,v) 上の k 番目の頂点
        (0-indexed)
        """

        l = self.lca(u, v)

        du = self.depth[u] - self.depth[l]
        dv = self.depth[v] - self.depth[l]

        if k > du + dv:
            return -1

        if k <= du:
            return self._ancestor(u, k)

        return self._ancestor(v, du + dv - k)

    def _ancestor(self, v, k):
        """
        v から k 個上へ
        """

        while True:

            h = self.head[v]

            if self.id[v] - k >= self.id[h]:
                return self.vertex[self.id[v] - k]

            k -= (
                self.id[v]
                - self.id[h]
                + 1
            )

            v = self.parent[h]


# ========= サンプル =========
n = 5
# (to, weight)
g = [[] for _ in range(n)]
edges = [(0, 1, 3),(0, 2, 5),(1, 3, 2),(1, 4, 7),]
"""visualize
5 4
0 1 3
0 2 5
1 3 2
1 4 7
"""

for u, v, w in edges:
    g[u].append(v)
    g[v].append(u)
hld = HLD(n, g)
print(f"{hld.vertex=}")    

### 頂点属性 ###
A = [0, 1, 2, 3, 4]
init_vertex = [A[v] for v in hld.vertex]
LR_vertex = hld.path_ranges(2, 3, edge=False)
print(f"{init_vertex=}")    
print(f"2-3: {LR_vertex=}")    
#################

### 辺属性 ###
A = [0] * n
for u, v, w in edges:
    # 辺の情報を、深い側の頂点に属するものとして扱う
    if hld.depth[u] > hld.depth[v]: u, v = v, u
    A[v] = w
init_path = [A[v] for v in hld.vertex]
LR_path = hld.path_ranges(2, 3, edge=True)
print(f"{init_path=}")    
print(f"2-3: {LR_path=}")    
################
