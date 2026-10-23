
import random
class Node:
    __slots__ = ("val", "pri", "size", "left", "right", "rev")

    def __init__(self, val):
        self.val = val
        self.pri = random.random()
        self.size = 1
        self.left = None
        self.right = None
        self.rev = False


def size(t):
    return t.size if t else 0


def update(t):
    if t:
        t.size = 1 + size(t.left) + size(t.right)


def push(t):
    if t and t.rev:
        t.left, t.right = t.right, t.left
        if t.left:
            t.left.rev ^= True
        if t.right:
            t.right.rev ^= True
        t.rev = False


def merge(l, r):
    if not l or not r:
        return l or r
    push(l)
    push(r)
    if l.pri > r.pri:
        l.right = merge(l.right, r)
        update(l)
        return l
    else:
        r.left = merge(l, r.left)
        update(r)
        return r


def split(t, k):
    if not t:
        return None, None
    push(t)
    if size(t.left) >= k:
        l, t.left = split(t.left, k)
        update(t)
        return l, t
    else:
        t.right, r = split(t.right, k - size(t.left) - 1)
        update(t)
        return t, r


class ImplicitTreap:
    def __init__(self):
        self.root = None

    def size(self):
        return size(self.root)

    def insert(self, i, x):
        l, r = split(self.root, i)
        self.root = merge(merge(l, Node(x)), r)

    def erase(self, i):
        l, r = split(self.root, i)
        m, r = split(r, 1)
        self.root = merge(l, r)
        return m.val

    def get(self, i):
        t = self.root
        while t:
            push(t)
            s = size(t.left)
            if i < s:
                t = t.left
            elif i == s:
                return t.val
            else:
                i -= s + 1
                t = t.right
        raise IndexError("index out of range")

    def set(self, i, x):
        t = self.root
        while t:
            push(t)
            s = size(t.left)
            if i < s:
                t = t.left
            elif i == s:
                t.val = x
                return
            else:
                i -= s + 1
                t = t.right
        raise IndexError("index out of range")

    def reverse(self, l, r):
        a, b = split(self.root, l)
        m, c = split(b, r - l)
        if m:
            m.rev ^= True
        self.root = merge(merge(a, m), c)

    def to_list(self):
        res = []
        stack = []
        t = self.root
        while stack or t:
            while t:
                push(t)
                stack.append(t)
                t = t.left
            t = stack.pop()
            res.append(t.val)
            t = t.right
        return res
