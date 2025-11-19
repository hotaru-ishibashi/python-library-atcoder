from typing import List, Dict
from random import randrange

class RangeMultiSetHash:
    def __init__(self, V: List[int], table: Dict[int, int]):
        self.csum = [0]
        for e in V:
            if not e in table:
                table[e] = randrange(1<<60)
        # seen = set()
        for e in V:
            self.csum.append(self.csum[-1] + table[e])    

    def hash(self, l, r):
        return self.csum[r] - self.csum[l]
table = {}
rsh = RangeMultiSetHash([1, 2, 3, 2, 3], table)

print(rsh.hash(1, 3) == rsh.hash(3, 5))