class Affine:
    affine = [1, 0, 0, 0, 1, 0, 0, 0, 1]
    def __init__(self):
        pass

    def apply(self, x, y):
        x_ = x * self.affine[0] + y * self.affine[3] + self.affine[6]
        y_ = x * self.affine[1] + y * self.affine[4] + self.affine[7]
        return x_, y_

    """
    new_x = ax + by + p
    new_y = cx + dy + q
    """
    def convert(self, a, b, p, c, d, q):
        mat = [
            a, c, 0,
            b, d, 0,
            p, q, 1,
        ]
        self.compose(mat)

    """
    時計回りに90°回転
    """
    def rotate90(self):
        mat = [0, 1, 0, 
               -1, 0, 0, 
               0, 0, 1]
        self.compose(mat)

    """
    反時計回りに90°回転
    """
    def rotate90cc(self):
        mat = [0, -1, 0, 
               1, 0, 0, 
               0, 0, 1]
        self.compose(mat)

    """
    X=xを基準にflip
    """
    def flipX(self, x=0):
        mat = [-1, 0, x, 
               0, 1, 0, 
               0, 0, 1]
        self.compose(mat)

    def flipY(self, y=0):
        mat = [1, 0, 0, 
               0, -1, y, 
               0, 0, 1]
        self.compose(mat)

    def compose(self, mat):
        self.affine = self.mul(self.affine, mat)

    def mul(self, M, N):
        L = [0] * 9
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    L[i*3+j] += M[i*3+k] * N[k*3+j]
        return L
    
if __name__ == "__main__":
    af = Affine()
    af.rotate90()
    print(af.affine)