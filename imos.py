class IMOS:
    def __init__(self, N):
        self.arr = [0] * N

    def add(self, L, R, v=1):
        """ [L, R) にvを加算する
        """
        self.arr[L] += v
        if R < len(self.arr):
            self.arr[R] -= v


    def calc(self):
        """ 区間加算結果を計算。O(N)
        """
        res = []
        csum = 0
        for a in self.arr:
            csum += a
            res.append(csum)
        return res
    

class IMOS2D:
    def __init__(self, H, W):
        self.grid = [[0] * (W+1) for _ in range(H+1)]
        self.H = H
        self.W = W

    def add(self, top, left, bottom, right, v=1):
        """ 矩形範囲 [top, bottom), [left, right) にvを加算する
        """
        self.grid[top][left] += v
        self.grid[top][right] -= v
        self.grid[bottom][left] -= v
        self.grid[bottom][right] += v

    def calc(self):
        """ 区間加算結果を計算。O(H*W)
        """
        res = [[0] * self.W for _ in range(self.H)]
        for i in range(self.H):
            csum = 0
            for j in range(self.W):
                csum += self.grid[i][j]
                res[i][j] = csum
        for j in range(self.W):
            for i in range(1, self.H):
                res[i][j] += res[i-1][j]
        return res
    