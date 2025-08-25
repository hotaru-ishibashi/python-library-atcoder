from atcoder.segtree import SegTree

class Node:
    def __init__(self, val=0):
        self.val = val
        pass
    
def op(n1, n2):
    nn = Node()
    nn.val = n1.val + n2.val
    return nn

e = Node()

A = [1, 3, 5, -5, 15]
vals = []
for a in A:
    node = Node(a)
    vals.append(node)

tree = SegTree(op, e, vals)