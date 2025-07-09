

class PotentializedUF:
    def __init__(self, n: int):
        self.par = [-1] * n
        self.weight = [0] * n

    def root(self, x: int):
        if self.par[x] < 0:
            return x
        
        r = self.root(self.par[x])
        self.weight[x] += self.weight[self.par[x]]
        self.par[x] = r

        return r
    
    def same(self, x: int, y: int):
        return self.root(x) == self.root(y)
    
    def size(self, x: int):
        return -self.par[self.root(x)]
    
    def merge(self, x: int, y: int, w: int):
        w += self.get_weight(x)
        w -= self.get_weight(y)
        x = self.root(x)
        y = self.root(y)

        if x == y:
            return False

        if self.par[x] > self.par[y]:
            x, y = y, x
            w = -w
        
        self.par[x] += self.par[y]
        self.par[y] = x
        self.weight[y] = w

        return True
    
    def get_weight(self, x: int):
        self.root(x)
        return self.weight[x]
    
    def get_diff(self, x: int, y: int):
        return self.get_weight(x) - self.get_weight(y)