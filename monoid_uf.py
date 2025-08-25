from collections import defaultdict


class MonoidUF:
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