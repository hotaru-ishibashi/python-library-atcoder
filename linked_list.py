

class UniqueLinkedList:
    def __init__(self):
        self.nodes = {}
        self.head = None
        self.tail = None

    def appendleft(self, val):
        assert not (val in self.nodes)
        if self.head is None:
            self.nodes[val] = [None, None]
            self.head = val
            self.tail = val
            return
        curhead = self.head
        self.nodes[curhead][0] = val
        self.nodes[val] = [None, curhead]

    def append(self, val):
        assert not (val in self.nodes)
        if self.tail is None:
            self.nodes[val] = [None, None]
            self.head = val
            self.tail = val
            return
        curtail = self.tail
        self.nodes[curtail][1] = val
        self.nodes[val] = [curtail, None]

    """
    keyの要素の直後に挿入する
    """
    def insert_after(self, key, val):
        assert (not (val in self.nodes) and key in self.nodes)

        self.nodes[val] = [None, None]
        if self.nodes[key][1] is not None:
            curnext = self.nodes[key][1]
            self.nodes[curnext][0] = val
            self.nodes[val][1] = curnext

        self.nodes[key][1] = val
        self.nodes[val][0] = key

    
    def delete(self, key):
        assert key in self.nodes

        curprev, curnext = self.nodes[key]
        
        self.nodes[curprev][1] = curnext
        self.nodes[curnext][0] = curprev

