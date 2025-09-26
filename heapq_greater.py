from heapq import heappop, heappush
class _MaxHeapWrapper:
    """オブジェクトをラップして、逆順比較を定義する"""
    __slots__ = ("obj",)
    def __init__(self, obj):
        self.obj = obj
    def __lt__(self, other: "_MaxHeapWrapper"):
        return self.obj > other.obj  # 比較を反転
    def __repr__(self):
        return f"_MaxHeapWrapper({self.obj!r})"

class GreaterHeapQue:
    def __init__(self, arr):
        self.que = []
        for a in arr:
            self.push(a)

    def pop(self):
        return heappop(self.que).obj
    
    def push(self, val):
        heappush(self.que, _MaxHeapWrapper(val))

    def top(self):
        return self.que[0].obj

    def __repr__(self):
        return [val.obj for val in self.que].__repr__()
