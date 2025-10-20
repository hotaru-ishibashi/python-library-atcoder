from typing import Any, Callable, List

class Rerooting:
    def __init__(self, n: int):
        self.n = n
        self.adj: List[List[int]] = [[] for _ in range(n)]

    def add_edge(self, u: int, v: int) -> None:
        self.adj[u].append(v)
        self.adj[v].append(u)

    def solve(
        self,
        merge: Callable[[Any, Any], Any],
        add: Callable[[Any, int, int], Any],
        e: Any,
        root: int = 0
    ) -> List[Any]:
        n = self.n
        dp_down = [e for _ in range(n)]
        Kids = [[] for _ in range(n)]
        parent = [-1] * n
        order = []

        # --- dfs1: 行きがけ順 + 帰りがけ処理をstackで ---
        stack = [(root, 0)]  # (v, state) state=0: 行きがけ, 1: 帰りがけ
        while stack:
            v, state = stack.pop()
            if state == 0:
                order.append(v)
                stack.append((v, 1))
                for nv in self.adj[v]:
                    if nv == parent[v]:
                        continue
                    parent[nv] = v
                    stack.append((nv, 0))
            else:
                acc = e
                for nv in self.adj[v]:
                    if nv == parent[v]:
                        continue
                    transformed = add(dp_down[nv], nv, v)
                    Kids[v].append((nv, transformed))
                    acc = merge(acc, transformed)
                dp_down[v] = acc

        # --- dfs2: 再根DP伝搬 ---
        res = [e for _ in range(n)]
        stack = [(root, e)]  # (v, up_value)

        while stack:
            v, up_value = stack.pop()
            m = len(Kids[v])
            prefix = [e] * (m + 1)
            suffix = [e] * (m + 1)

            for i in range(m):
                prefix[i + 1] = merge(prefix[i], Kids[v][i][1])
            for i in range(m - 1, -1, -1):
                suffix[i] = merge(Kids[v][i][1], suffix[i + 1])

            res[v] = merge(prefix[m], up_value)

            # 各子に伝搬
            for i, (nv, _) in enumerate(Kids[v]):
                combined = merge(prefix[i], suffix[i + 1])
                combined_with_up = merge(combined, up_value)
                child_up = add(combined_with_up, v, nv)
                stack.append((nv, child_up))

        return res
    

# example: ABC428-E 最遠かつ頂点番号最大の頂点
if __name__ == "__main__":
    N = int(input())
    reroot = Rerooting(N)
    for _ in range(N-1):
        u, v = map(int, input().split())
        u -= 1; v -= 1
        reroot.add_edge(u, v)

    """モノイドの合成"""
    def merge(a, b):
        return max(a, b)

    """
    子頂点の値から親頂点の値を導出
    """
    def add(child_dp, child, parent):
        if child_dp == e:
            return (child_dp[0]+1, child)
        else:
            return (child_dp[0]+1, child_dp[1])

    e = (0, -1)

    ans = reroot.solve(merge, add, e)
