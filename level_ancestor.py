class LevelAncestor:
    def __init__(self, graph, root=0):
        """
        graph: 隣接リスト（無向木）
        root: 根ノード
        """
        n = len(graph)
        self.LOG = (n).bit_length()
        self.parent = [[-1] * n for _ in range(self.LOG)]
        self.depth = [0] * n

        # --- 非再帰DFSで親と深さを求める ---
        stack = [(root, -1, 0)]
        while stack:
            v, p, d = stack.pop()
            self.parent[0][v] = p
            self.depth[v] = d
            for nv in graph[v]:
                if nv == p:
                    continue
                stack.append((nv, v, d + 1))

        # --- ダブリングテーブル構築 ---
        for k in range(1, self.LOG):
            pk = self.parent[k - 1]
            for v in range(n):
                pv = pk[v]
                self.parent[k][v] = -1 if pv == -1 else pk[pv]

    def query(self, v, k):
        """
        頂点 v の k 代先祖を返す。存在しなければ -1。
        O(logN)
        """
        for i in range(self.LOG):
            if k >> i & 1:
                v = self.parent[i][v]
                if v == -1:
                    return -1
        return v