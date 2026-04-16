class Affine:
    def __init__(self):
        self.affine = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

    def apply(self, x, y):
        x_ = x * self.affine[0][0] + y * self.affine[1][0] + self.affine[2][0]
        y_ = x * self.affine[0][1] + y * self.affine[1][1] + self.affine[2][1]
        return x_, y_

    """
    new_x = ax + by + p
    new_y = cx + dy + q
    """
    def convert(self, a, b, p, c, d, q):
        mat = [
            [a, c, 0],
            [b, d, 0],
            [p, q, 1],
        ]
        self.compose(mat)

    """
    半時計回りに90°回転
    """
    def rotate90(self):
        mat = [[0, 1, 0], 
               [-1, 0, 0], 
               [0, 0, 1]]
        self.compose(mat)

    """
    時計回りに90°回転
    """
    def rotate90cc(self):
        mat = [[0, -1, 0], 
               [1, 0, 0], 
               [0, 0, 1]]
        self.compose(mat)

    """
    X=xを基準にflip
    """
    def flipX(self, x=0):
        mat = [[-1, 0, x], 
               [0, 1, 0], 
               [0, 0, 1]]
        self.compose(mat)

    def flipY(self, y=0):
        mat = [[1, 0, 0], 
               [0, -1, y], 
               [0, 0, 1]]
        self.compose(mat)

    def compose(self, mat):
        self.affine = self.mul(self.affine, mat)

    def mul(self, M, N):
        n1 = len(M)
        n2 = len(M[0])
        n3 = len(N[0])
        L = [[0] * n3 for _ in range(n1)]
        for i in range(n1):
            for j in range(n3):
                for k in range(n2):
                    L[i][j] = (L[i][j] + M[i][k] * N[k][j])
        return L