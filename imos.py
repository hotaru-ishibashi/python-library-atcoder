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
        cs = [0]
        for a in self.arr:
            cs.append(cs[-1] + a)
        self.csum = cs
        return cs
    
    """
    区間和[l, r)を計算 事前にimos.calc()すること
    """ 
    def seg_sum(self, l, r):
        if not self.csum:
            raise ValueError("calc first")
        return self.csum[r] - self.csum[l]

class IMOS2D:
    csum = None
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
        res = [[0] * (self.W + 1) for _ in range(self.H + 1)]
        for i in range(self.H):
            csum = 0
            for j in range(self.W):
                csum += self.grid[i][j]
                res[i+1][j+1] = csum
        for j in range(self.W+1):
            for i in range(1, self.H+1):
                res[i][j] += res[i-1][j]
        self.csum = res
        return res
    
    """ 矩形範囲内 [top, bottom), [left, right)] の合計を計算 O(1)
        事前にimos.calc()が必要
    """
    def rect_sum(self, top, left, bottom, right):
        if not self.csum:
            raise ValueError("calc first")
        # print(top, left, bottom, right)
        m = self.csum[bottom][right]
        t = self.csum[top][right]
        l = self.csum[bottom][left]
        tl = self.csum[top][left]
    
        return m - t - l + tl            
    

class IMOS3D:
    def __init__(self, X, Y, Z):
        self.X = X
        self.Y = Y
        self.Z = Z
        # +1してバッファを持たせる
        self.grid = [[[0] * (Z + 1) for _ in range(Y + 1)] for _ in range(X + 1)]

    def add(self, x_start, y_start, z_start, x_end, y_end, z_end, v=1):
        """
        立方体領域 [x_start, x_end), [y_start, y_end), [z_start, z_end) に v を加算
        """
        g = self.grid
        g[x_start][y_start][z_start] += v
        g[x_start][y_start][z_end]   -= v
        g[x_start][y_end][z_start]   -= v
        g[x_start][y_end][z_end]     += v
        g[x_end][y_start][z_start]   -= v
        g[x_end][y_start][z_end]     += v
        g[x_end][y_end][z_start]     += v
        g[x_end][y_end][z_end]       -= v

    def calc(self):
        """
        区間加算結果を計算。O(X*Y*Z)
        """
        res = [[[0] * self.Z for _ in range(self.Y)] for _ in range(self.X)]
        # x方向に累積和
        for x in range(self.X):
            for y in range(self.Y):
                csum = 0
                for z in range(self.Z):
                    csum += self.grid[x][y][z]
                    res[x][y][z] = csum
        # y方向に累積和
        for x in range(self.X):
            for y in range(1, self.Y):
                for z in range(self.Z):
                    res[x][y][z] += res[x][y-1][z]
        # z方向に累積和
        for x in range(1, self.X):
            for y in range(self.Y):
                for z in range(self.Z):
                    res[x][y][z] += res[x-1][y][z]
        return res
