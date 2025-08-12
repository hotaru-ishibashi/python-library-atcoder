from time import time

class Ternary:
    p = []
    def __init__(self, N, iniVal=None):
        self.N = N
        self.state = 0
        for i in range(N):
            self.p.append(3**i)
        if iniVal is not None:
            for i in range(N):
                self.set(i, iniVal[i])
    def get(self, i):
        # assert 0 <= i < self.N
        return self.state//self.p[i]%3

    def set(self, i, v):
        # assert 0 <= i < self.N
        # assert 0 <= v < 3
        self.state -= self.get(i) * self.p[i]
        self.state += v * self.p[i]

    def __repr__(self):
        return "".join([str(self.get(i)) for i in range(self.N)])

    def __hash__(self):
        return hash(self.state)
    
t1 = Ternary(9)
t1.state = 256248
s = 256428
p = time()
for i in range(10000):
    t1.get(4)
print(time()-p)

p = time()
for i in range(10000):
    s//(3**4)%3
print(time()-p)