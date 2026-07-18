class Line:
    __slots__ = ("a", "b", "c")

    def __init__(self, *args):
        if len(args) == 2:
            # 2点 (x1,y1), (x2,y2)
            (x1, y1), (x2, y2) = args
            a = y1 - y2
            b = x2 - x1
            c = -(a * x1 + b * y1)
        elif len(args) == 3:
            a, b, c = args
        else:
            raise TypeError("Line((x1,y1),(x2,y2)) or Line(a,b,c)")

        if a == 0 and b == 0:
            raise ValueError("invalid line")

        g = gcd(gcd(abs(a), abs(b)), abs(c))
        if g:
            a //= g
            b //= g
            c //= g

        # 符号を統一
        if a < 0 or (a == 0 and b < 0):
            a, b, c = -a, -b, -c

        self.a = a
        self.b = b
        self.c = c

    def contains(self, p):
        x, y = p
        return self.a * x + self.b * y + self.c == 0

    def cross_point(self, other):
        """
        平行なら None
        交点があれば (x, y) を返す (float)
        """
        det = self.a * other.b - other.a * self.b
        if det == 0:
            return None

        x = (self.b * other.c - other.b * self.c) / det
        y = (other.a * self.c - self.a * other.c) / det
        return (x, y)

    def same(self, other):
        return (
            self.a == other.a
            and self.b == other.b
            and self.c == other.c
        )
        
    @staticmethod
    def perpendicular_bisector(p1, p2):
        """
        線分 p1-p2 の垂直二等分線を返す
        """
        x1, y1 = p1
        x2, y2 = p2

        if (x1, y1) == (x2, y2):
            raise ValueError("points must be distinct")

        dx = x2 - x1
        dy = y2 - y1

        # 法線ベクトルは元の方向ベクトル (dx, dy)
        a = dx
        b = dy
        c = -(dx * (x1 + x2) + dy * (y1 + y2))

        # 2倍しているので偶数なら割る
        if a % 2 == 0 and b % 2 == 0 and c % 2 == 0:
            a //= 2
            b //= 2
            c //= 2

        return Line(a, b, c)

    def __repr__(self):
        return f"Line({self.a}, {self.b}, {self.c})"
