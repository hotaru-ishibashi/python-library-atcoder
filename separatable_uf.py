from collections import defaultdict


class OperationalUF:
    def __init__(self, n: int, op, vals):
        self.n = n
        self.par = [-1] * n
        self.weight = [0] * n
        self.op = op
        self.vals = vals

    def leader(self, x: int):
        if self.par[x] < 0:
            return x
        
        r = self.leader(self.par[x])
        self.par[x] = r

        return r
    
    def same(self, x: int, y: int):
        return self.leader(x) == self.leader(y)
    
    def size(self, x: int):
        return -self.par[self.leader(x)]
    
    def merge(self, x: int, y: int):
        x = self.leader(x)
        y = self.leader(y)
        if x == y:
            return False
        if self.par[x] > self.par[y]:
            x, y = y, x

        self.vals[x] = self.op(self.vals[x], self.vals[y])
        
        self.par[x] += self.par[y]
        self.par[y] = x

        return True
    
    def get_value(self, x: int):
        return self.vals[self.leader(x)]
    
    def set_value(self, x: int, value):
        self.vals[self.leader(x)] = value

    def __repr__(self):
        groups = self.groups()
        res = []
        for root in groups.keys():
            res.append(f"代表元: {root}, 集計値: {self.get_value(root)}, 要素数: {len(groups[root])}")
        return " / ".join(res)
    
    def groups(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.leader(member)].append(member)
        return group_members


class SeparatableUF:
    """
    N: 初期要素数
    Q: 削除されうる回数の上限
    """
    def __init__(self, N, Q):
        self.uf = OperationalUF(N+Q, lambda x, y: x+y, [1] * (N+Q))
        self.ref = [i for i in range(N)]
        self.next_v = N

    def leader(self, x: int):
        x = self.ref[x]
        return self.uf.leader(x)
    
    def same(self, x: int, y: int):
        x, y = self.ref[x], self.ref[y]
        return self.uf.same(x, y)
    
    def size(self, x: int):
        x = self.ref[x]
        return self.uf.get_value(x)
    
    def merge(self, x: int, y: int):
        x, y = self.ref[x], self.ref[y]

        return self.uf.merge(x, y)
    
    def delete(self, x):
        newx = self.next_v
        self.next_v += 1
        
        cx = self.ref[x]
        self.uf.set_value(cx, self.uf.get_value(cx)-1)

        self.ref[x] = newx


N, Q = map(int, input().split())
uf = SeparatableUF(N, Q)
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a, b = query[1:]
        a-=1; b-=1
        uf.merge(a, b)
    elif query[0] == 2:
        a = query[1] - 1
        print(uf.size(a))
    elif query[0] == 3:
        a = query[1] - 1
        uf.delete(a)
