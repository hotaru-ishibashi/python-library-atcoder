


def sub_tree_map(T, root, vertex_info):
    '''
    lr_memo: { 元の頂点番号v: ↓におけるvの部分木に対応する(l, r) }
             
    V_euler_order: 頂点情報をオイラー順(行きがけのみ)に並べた配列
    '''
    lr_memo = {}
    hist = []
    stack = [(root, -1, 0)]  # (node, parent, state) state=0:入る前, 1:出るとき
    V_euler_order = []

    while stack:
        v, pre, state = stack.pop()
        if state == 0:
            # 入るタイミング
            lr_memo[v] = [len(hist), -1]
            hist.append(v)
            V_euler_order.append(vertex_info[v])
            # 出るタイミングを後で処理するため再プッシュ
            stack.append((v, pre, 1))
            # 子ノードを逆順にpush（先に左の子を処理したい場合）
            for nv in reversed(T[v]):
                if nv == pre:
                    continue
                stack.append((nv, v, 0))
        else:
            # 出るタイミング
            lr_memo[v][1] = len(hist)

    return lr_memo, V_euler_order

    

T = [
    [1, 2],
    [0],
    [0]
]
V = [1, 3, 8]

lr, V_euler_order = sub_tree_map(T, 2, V)
print(V_euler_order)
from atcoder.segtree import SegTree
tree = SegTree(lambda x, y: x+y, 0, V_euler_order)
# 頂点1の部分木に対応する区間クエリ
tree.prod(lr[1])
# 頂点1の値を更新
tree.set(lr[1][0], 5)
