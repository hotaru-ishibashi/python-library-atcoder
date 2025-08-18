
"""
正規化されたpolyomino
"""
class MINO:
    onstr = "#"
    offstr = "."
    top = 10**9
    bottom = -1
    left = 10**9
    right = -1

    def __init__(self, mino, H, W):
        self.mino = mino
        self.H = H
        self.W = W
        for i in range(H):
            for j in range(W):
                if self.mino&1<<(i*self.W + j):
                    self.top = min(self.top, i)
                    self.bottom = max(self.bottom, i)
                    self.left = min(self.left, j)
                    self.right = max(self.right, j)
        self.move_top_left()

    @staticmethod
    def fromGridStr(S, sheet_H=None, sheet_W=None, on="#"):
        H = len(S)
        W = len(S[0])
        sheet_H = H if sheet_H is None else sheet_H
        sheet_W = W if sheet_W is None else sheet_W

        mino = 0 
        for i in range(H):
            for j in range(W):
                if S[i][j] == on:
                    mino |= 1<<(i*sheet_W + j)
        return MINO(mino, sheet_H, sheet_W)
    

    def rotated(self, rotate_num):
        res = 0
        rotate_num %= 4

        if rotate_num == 0:
            res = self.mino
        else:
            for i in range(self.H):
                for j in range(self.W):
                    if self.mino&1<<(i*self.W + j):
                        if rotate_num == 1:
                            shift = (j*self.W + (self.W-1-i))
                        elif rotate_num == 2:
                            shift = ((self.H-1-i)*self.W + (self.W-1-j))
                        elif rotate_num == 3:
                            shift = ((self.H-1-j)*self.W + i)
                        res |= 1 << shift
        newH, newW = (self.W, self.H) if rotate_num%2 == 1 else (self.H, self.W)
        r = MINO(res, newH, newW)
        r.move_top_left()
        return r

    
    def flipped_horizontal(self):
        res = 0
        for i in range(self.H):
            for j in range(self.W):
                if self.mino&1<<(i*self.W + j):
                    shift = (i*self.W + (self.W-1-j))
                res |= 1 << shift
        r = MINO(res, self.H, self.W)
        r.move_top_left()
        return r

    def flipped_vertical(self):
        res = 0
        for i in range(self.H):
            for j in range(self.W):
                if self.mino&1<<(i*self.W + j):
                    shift = ((self.H-1-i)*self.W + j)
                res |= 1 << shift
        r = MINO(res, self.H, self.W)
        r.move_top_left()
        return r

    def rotations(self):
        """90/180/270°回転によって取り得るMINOの値"""
        res = set()
        res.add(self)
        for i in range(1, 4):
            res.add(self.rotated(i))
        return res
    
    def moved(self, di, dj):
        """di, djだけ平行移動した場合の集合bit値"""
        shift = (di*self.W + dj)
        return self.mino << shift if shift >= 0 else self.mino >> abs(shift)
    
    def translations(self):
        """範囲内の平行移動で取り得る集合bit値"""
        irange = self.H - self.bottom 
        jrange = self.W - self.right 
        res = [[None] * jrange for _ in range(irange)]
        resset = set()
        for i in range(irange):
            for j in range(jrange):
               moved = self.moved(i, j) 
               res[i][j] = moved
               resset.add(moved)

        return res, resset
        
    def can_move(self, di, dj):
        return self.bottom+di < self.H and self.right+dj < self.W and self.top+di >= 0 and self.left+dj >= 0

    def move(self, di, dj):
        if not self.can_move(di, dj):
            return False
        self.mino = self.moved(di, dj)
        self.top += di; self.bottom += di
        self.left += dj; self.right +=dj
        
        return True
    
    def move_top_left(self):
        while self.move(-1, 0):
            pass
        while self.move(0, -1):
            pass

    @staticmethod
    def toStr(mino, H, W):
        res = []
        for i in range(H):
            row = []
            for j in range(W):
                val = "#" if mino&1<<(i*W + j) else "."
                row.append(val)
            res.append("".join(row))
        return "\n".join(res)

    def __repr__(self):
        return self.toStr(self.mino, self.H, self.W)

        
    def __hash__(self):
        return hash(self.mino)

    def __eq__(self, value):
        return self.mino == value.mino