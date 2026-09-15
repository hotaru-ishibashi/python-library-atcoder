class UniqueLinkedList:
    def __init__(self):
        self.nodes = {}
        self.head = None
        self.tail = None

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
        self.tail = val

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
        if curprev is not None:
            self.nodes[curprev][1] = curnext
        else:
            self.head = curnext

        if curnext is not None:
            self.nodes[curnext][0] = curprev
        else:
            self.tail = curprev

        del self.nodes[key]
