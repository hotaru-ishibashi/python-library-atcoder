from math import gcd, hypot

class Line:
    """
    ax + by + c = 0
    """

    __slots__ = ("a", "b", "c")

    def __init__(self, *args):
        if len(args) == 2:
            # Line((x1,y1), (x2,y2))
            (x1, y1), (x2, y2) = args
            if (x1, y1) == (x2, y2):
                raise ValueError("points must be distinct")

            a = y1 - y2
            b = x2 - x1
            c = -(a * x1 + b * y1)

        elif len(args) == 3:
            # Line(a, b, c)
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

        if a < 0 or (a == 0 and b < 0):
            a, b, c = -a, -b, -c

        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def perpendicular_bisector(p1, p2):
        """
        p1 ●────×────● p2
                 │
                 │
                 │
        """
        x1, y1 = p1
        x2, y2 = p2

        if (x1, y1) == (x2, y2):
            raise ValueError("points must be distinct")

        dx = x2 - x1
        dy = y2 - y1

        a = dx
        b = dy
        c = -(dx * (x1 + x2) + dy * (y1 + y2))

        if a % 2 == b % 2 == c % 2 == 0:
            a //= 2
            b //= 2
            c //= 2

        return Line(a, b, c)

    @staticmethod
    def through_point_parallel(line, p):
        """
               ● p
        ───────────────
           ↑ parallel
        ───────────────
        """
        x, y = p
        a, b = line.a, line.b
        c = -(a * x + b * y)
        return Line(a, b, c)

    @staticmethod
    def through_point_perpendicular(line, p):
        """
               │
               │
               ● p
        ───────┼───────
               │
               │
        """
        x, y = p
        a = -line.b
        b = line.a
        c = -(a * x + b * y)
        return Line(a, b, c)

    @property
    def direction(self):
        """
        direction →
        ────────────
        """
        return (-self.b, self.a)

    def contains(self, p):
        """● on line ?"""
        x, y = p
        return self.a * x + self.b * y + self.c == 0

    def side(self, p):
        """
             +
        ───────────
             -
        """
        x, y = p
        v = self.a * x + self.b * y + self.c
        return (v > 0) - (v < 0)

    def is_parallel(self, other):
        """
        ───────────
        ───────────
        """
        return self.a * other.b == self.b * other.a

    def is_perpendicular(self, other):
        """
             │
             │
        ─────┼─────
             │
        """
        return self.a * other.a + self.b * other.b == 0

    def cross_point(self, other):
        """
        \  /
         \/
         /\
        /  \

        parallel -> None
        """
        det = self.a * other.b - other.a * self.b
        if det == 0:
            return None

        x = (self.b * other.c - other.b * self.c) / det
        y = (other.a * self.c - self.a * other.c) / det
        return (x, y)

    def distance(self, p):
        """
        ●
        │ shortest
        │
        ───────────
        """
        x, y = p
        return abs(self.a * x + self.b * y + self.c) / hypot(self.a, self.b)

    def project(self, p):
        """
        ●
        │
        ×──────────
        """
        x, y = p
        t = -(self.a * x + self.b * y + self.c) / (
            self.a * self.a + self.b * self.b
        )
        return (x + self.a * t, y + self.b * t)

    def reflect(self, p):
        """
        ●
        │
        ×──────────
        │
        ●
        """
        x, y = p
        t = -2 * (self.a * x + self.b * y + self.c) / (
            self.a * self.a + self.b * self.b
        )
        return (x + self.a * t, y + self.b * t)

    def __eq__(self, other):
        if not isinstance(other, Line):
            return NotImplemented
        return (
            self.a == other.a
            and self.b == other.b
            and self.c == other.c
        )

    def __repr__(self):
        return f"Line({self.a}, {self.b}, {self.c})"
    
    def __hash__(self):
        return hash((self.a, self.b, self.c))