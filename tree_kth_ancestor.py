LOG = 20  # 2^20 > 10^6 なら十分。必要に応じて調整。

def build_doubling(root, G):
    N = len(G)
    parent = [[-1] * N for _ in range(LOG)]  # parent[k][v] = v の 2^k 個上の祖先
    depth = [0] * N

    # --- BFS or DFS で parent[0] と depth を求める ---
    stack = [root]
    parent[0][root] = -1
    depth[root] = 0
    order = []                 # 探索順を記録して後から使う

    while stack:
        v = stack.pop()
        order.append(v)
        for w in G[v]:
            if w == parent[0][v]:
                continue
            parent[0][w] = v
            depth[w] = depth[v] + 1
            stack.append(w)

    # --- ダブリング表を作る ---
    for k in range(1, LOG):
        for v in order:
            p = parent[k - 1][v]
            parent[k][v] = -1 if p == -1 else parent[k - 1][p]

    return parent, depth


def kth_ancestor(v, k, parent):
    LOG = len(parent)
    for i in range(LOG):
        if k & (1 << i):
            v = parent[i][v]
            if v == -1:
                break
    return v