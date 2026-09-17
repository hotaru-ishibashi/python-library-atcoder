# Codon-safe SA-IS SuffixArray (ints only)
# - input: List[int] (you can pass [ord(c) for c in s] for strings)
# - returns:
#   - idx, rank, hgt
#   - search_pattern: position or -1
#   - search_pattern_all: list of positions
#   - traverse, repeated_substring, longest_repeated_substring

class SuffixArray:
    buff: list[int]
    size: int
    idx: list[int]
    rank: list[int]
    hgt: list[int]
    def __init__(self, buff):  # buff: List[int]
        self.buff = buff
        self.size = len(buff)

        # ---- integerize + sentinel 0 ----
        # shift to be >= 1, sentinel = 0
        s = []
        if self.size == 0:
            s = []
        else:
            minv = buff[0]
            for x in buff:
                if x < minv:
                    minv = x
            if minv < 0:
                off = 1 - minv
                for x in buff:
                    s.append(x + off)
            else:
                for x in buff:
                    s.append(x + 1)

        s.append(0)

        K = 0
        for x in s:
            if x > K:
                K = x
        K += 1

        sa_full = self._sais(s, K)   # length N+1, first is sentinel pos (=N)
        self.idx = sa_full[1:]       # drop empty suffix

        self.rank = [0] * self.size
        for i in range(self.size):
            pos = self.idx[i]
            self.rank[pos] = i

        self.hgt = self._kasai(self.idx, s)

    # ---- bucket helpers ----
    def _bucket_ends(self, s, K):
        cnt = [0] * K
        for x in s:
            cnt[x] += 1
        end = [0] * K
        tot = 0
        for i in range(K):
            tot += cnt[i]
            end[i] = tot
        return cnt, end

    def _bucket_starts(self, cnt):
        K = len(cnt)
        start = [0] * K
        tot = 0
        for i in range(K):
            start[i] = tot
            tot += cnt[i]
        return start

    def _induce(self, s, K, isS, sa):
        n = len(s)

        cnt, _end = self._bucket_ends(s, K)
        start = self._bucket_starts(cnt)
        for i in range(n):
            j = sa[i] - 1
            if j >= 0 and (not isS[j]):
                c = s[j]
                sa[start[c]] = j
                start[c] += 1

        cnt, end = self._bucket_ends(s, K)
        for i in range(n - 1, -1, -1):
            j = sa[i] - 1
            if j >= 0 and isS[j]:
                c = s[j]
                end[c] -= 1
                sa[end[c]] = j

    def _sais(self, s, K):
        n = len(s)
        if n == 1:
            return [0]
        if n == 2:
            return [1, 0]  # always

        isS = [False] * n
        isLMS = [False] * n
        isS[n - 1] = True  # sentinel is S

        for i in range(n - 2, -1, -1):
            if s[i] < s[i + 1]:
                isS[i] = True
            elif s[i] == s[i + 1]:
                isS[i] = isS[i + 1]
            else:
                isS[i] = False

        for i in range(1, n):
            isLMS[i] = (not isS[i - 1]) and isS[i]

        sa = [-1] * n
        cnt, end = self._bucket_ends(s, K)
        for i in range(n):
            if isLMS[i]:
                c = s[i]
                end[c] -= 1
                sa[end[c]] = i

        self._induce(s, K, isS, sa)

        lms = []
        for i in range(1, n):
            if isLMS[i]:
                lms.append(i)

        lms_pos = []
        for p in sa:
            if p != -1 and isLMS[p]:
                lms_pos.append(p)

        lms_name = [-1] * n
        name = 0
        prev = -1

        for p in lms_pos:
            diff = False
            if prev == -1:
                diff = True
            else:
                i = 0
                while True:
                    if s[p + i] != s[prev + i]:
                        diff = True
                        break
                    a_is_lms = isLMS[p + i]
                    b_is_lms = isLMS[prev + i]
                    if a_is_lms != b_is_lms:
                        diff = True
                        break
                    if i > 0 and (a_is_lms or b_is_lms):
                        break
                    i += 1

            if diff:
                name += 1
                prev = p
            lms_name[p] = name - 1

        if name < len(lms):
            red = [0] * len(lms)
            for i in range(len(lms)):
                red[i] = lms_name[lms[i]]
            red.append(0)
            sa_red_full = self._sais(red, name + 1)
            sa_red = sa_red_full[1:]

            lms_sorted = [0] * len(lms)
            for i in range(len(sa_red)):
                lms_sorted[i] = lms[sa_red[i]]
        else:
            lms_sorted = [0] * len(lms)
            for p in lms:
                lms_sorted[lms_name[p]] = p

        sa = [-1] * n
        cnt, end = self._bucket_ends(s, K)
        for i in range(len(lms_sorted) - 1, -1, -1):
            p = lms_sorted[i]
            c = s[p]
            end[c] -= 1
            sa[end[c]] = p

        self._induce(s, K, isS, sa)
        return sa

    def _kasai(self, sa, s_with0):
        n = self.size
        rank = [0] * n
        for i in range(n):
            p = sa[i]
            if p < n:
                rank[p] = i

        h = 0
        lcp = [0] * n
        for i in range(n):
            r = rank[i]
            if r == n - 1:
                lcp[r] = -1
                h = 0
                continue
            j = sa[r + 1]
            while i + h < n and j + h < n and s_with0[i + h] == s_with0[j + h]:
                h += 1
            lcp[r] = h
            if h > 0:
                h -= 1
        return lcp

    # ---- public API ----
    def lcp(self, x, y):
        i = 0
        while x + i < self.size and y + i < self.size and self.buff[x + i] == self.buff[y + i]:
            i += 1
        return i

    def compare_pat(self, x, pat, pat_size):
        for i in range(pat_size):
            if x + i >= self.size:
                return 1
            a = pat[i]
            b = self.buff[x + i]
            if a < b:
                return -1
            if a > b:
                return 1
        return 0

    def search_pattern_sub(self, pat, pat_size):
        low = 0
        high = self.size - 1
        while low <= high:
            mid = (low + high) // 2
            r = self.compare_pat(self.idx[mid], pat, pat_size)
            if r == 0:
                return mid
            elif r > 0:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    def search_pattern(self, pat):
        pat_size = len(pat)
        x = self.search_pattern_sub(pat, pat_size)
        if x >= 0:
            return self.idx[x]
        return -1

    def search_pattern_all(self, pat):
        pat_size = len(pat)
        x = self.search_pattern_sub(pat, pat_size)
        if x < 0:
            return []
        s = x - 1
        while s >= 0 and self.compare_pat(self.idx[s], pat, pat_size) == 0:
            s -= 1
        e = x + 1
        while e < self.size and self.compare_pat(self.idx[e], pat, pat_size) == 0:
            e += 1
        res = []
        for i in range(s + 1, e):
            res.append(self.idx[i])
        return res

    def traverse(self, func):
        st = [(-1, -1)]
        for i in range(self.size):
            st.append((i, self.size - self.idx[i]))
            hi = self.hgt[i]
            x, h = st[len(st) - 1]
            while h > hi:
                func(self.buff, self.idx[x], h)
                st.pop()
                x, h = st[len(st) - 1]
            if hi > 0 and h < hi:
                st.append((i, hi))

    def repeated_substring(self, n, m):
        a = []
        st = [(0, -1, -1)]
        for i in range(self.size):
            st.append((1, i, self.size - self.idx[i]))
            c, x, h = st[len(st) - 1]
            hi = self.hgt[i]
            ci = 0
            while h > hi:
                ci += c
                if ci >= m and h >= n:
                    a.append((self.idx[x], h, ci))
                st.pop()
                c, x, h = st[len(st) - 1]
            if h == hi:
                st[len(st) - 1] = (c + ci, x, h)
            elif hi > 0 and h < hi:
                st.append((ci, i, hi))
        return a

    def longest_repeated_substring(self):
        max_pos = -1
        max_len = -1
        st = [(0, -1, -1)]
        for i in range(self.size):
            st.append((1, i, self.size - self.idx[i]))
            c, x, h = st[len(st) - 1]
            hi = self.hgt[i]
            ci = 0
            while h > hi:
                ci += c
                if ci >= 2 and h > max_len:
                    max_pos = self.idx[x]
                    max_len = h
                st.pop()
                c, x, h = st[len(st) - 1]
            if h == hi:
                st[len(st) - 1] = (c + ci, x, h)
            elif hi > 0 and h < hi:
                st.append((ci, i, hi))
        return max_pos, max_len

# Compressed Suffix Tree built from SA + LCP (Codon-friendly)
# - input: list[int]
# - internally appends a unique terminal symbol (min(buff)-1)
# - edges are labeled by slices of the internal buffer (start, end)

# Requires: the SuffixArray class you already pasted (ints only).

class CSTNode:
    parent: int
    depth: int                # string depth from root (number of symbols)
    start: int                # edge label [start:end) from parent to this node
    end: int
    children: dict[int, int]  # first symbol -> child node id
    # optional: suffix index for leaf (start position of suffix)
    suf: int

    def __init__(self, parent: int, depth: int, start: int, end: int):
        self.parent = parent
        self.depth = depth
        self.start = start
        self.end = end
        self.children = {}
        self.suf = -1


class CompressedSuffixTree:
    buff: list[int]           # internal buff with terminal
    n: int                    # len(buff)
    sa: SuffixArray
    nodes: list[CSTNode]
    root: int

    def __init__(self, buff: list[int]):
        # ---- add unique terminal ----
        if len(buff) == 0:
            term = 0
        else:
            mn = buff[0]
            for x in buff:
                if x < mn:
                    mn = x
            term = mn - 1  # unique smallest (not in buff)

        b2 = buff[:]  # copy
        #b2.append(term)

        self.buff = b2
        self.n = len(b2)

        # build SA on b2
        self.sa = SuffixArray(b2)

        # build CST
        self.nodes = []
        self.root = self._new_node(-1, 0, 0, 0)  # root
        self._build()

    def _new_node(self, parent: int, depth: int, start: int, end: int) -> int:
        self.nodes.append(CSTNode(parent, depth, start, end))
        return len(self.nodes) - 1

    def _add_child(self, parent: int, child: int):
        # key is first symbol on edge label
        st = self.nodes[child].start
        key = self.buff[st]
        self.nodes[parent].children[key] = child
        self.nodes[child].parent = parent

    def _add_leaf(self, parent: int, suf_start: int) -> int:
        # leaf depth = n - suf_start
        depth_parent = self.nodes[parent].depth
        start = suf_start + depth_parent
        end = self.n
        leaf = self._new_node(parent, self.n - suf_start, start, end)
        self.nodes[leaf].suf = suf_start
        self._add_child(parent, leaf)
        return leaf

    def _split_edge(self, parent: int, child: int, new_depth: int) -> int:
        # split parent->child so that new internal node has depth=new_depth
        # parent.depth < new_depth < child.depth
        p = parent
        c = child
        dp = self.nodes[p].depth
        # offset inside the edge label
        off = new_depth - dp

        # create mid node; it takes the first part of child's edge label
        old_start = self.nodes[c].start
        mid_start = old_start
        mid_end = old_start + off

        mid = self._new_node(p, new_depth, mid_start, mid_end)

        # rewire: parent -> mid -> child
        # remove child from parent's children, replace with mid
        key_parent = self.buff[mid_start]
        self.nodes[p].children[key_parent] = mid

        # adjust child edge label to start after the split
        self.nodes[c].start = mid_end
        # mid gets child as its child
        key_mid = self.buff[self.nodes[c].start]
        self.nodes[mid].children[key_mid] = c

        # parent pointers
        self.nodes[mid].parent = p
        self.nodes[c].parent = mid

        return mid

    def _build(self):
        sa_idx = self.sa.idx
        hgt = self.sa.hgt
        m = len(sa_idx)  # equals n (includes terminal)

        st = [self.root]   # stack of node ids along the previous suffix path
        lcp_prev = 0       # LCP(sa[i-1], sa[i])

        for i in range(m):
            suf = sa_idx[i]

            last_popped = -1
            while self.nodes[st[len(st) - 1]].depth > lcp_prev:
                last_popped = st.pop()

            top = st[len(st) - 1]

            if self.nodes[top].depth < lcp_prev:
                # split edge between top and the child that was just below it on the path
                # that child is last_popped (must exist)
                mid = self._split_edge(top, last_popped, lcp_prev)
                st.append(mid)
                parent = mid
            else:
                parent = top

            leaf = self._add_leaf(parent, suf)
            st.append(leaf)

            # update lcp_prev for next i: LCP(sa[i], sa[i+1])
            if i < m - 1 and hgt[i] > 0:
                lcp_prev = hgt[i]
            else:
                lcp_prev = 0


    # --------- Optional utilities ---------

    def follow(self, pattern: list[int]) -> int:
        # return node id if pattern is found as a prefix of some path, else -1
        v = self.root
        i = 0
        L = len(pattern)

        while i < L:
            key = pattern[i]
            if key not in self.nodes[v].children:
                return -1
            to = self.nodes[v].children[key]

            # walk along edge label
            a = self.nodes[to].start
            b = self.nodes[to].end
            while a < b and i < L:
                if self.buff[a] != pattern[i]:
                    return -1
                a += 1
                i += 1
            v = to

        return v

    def _collect_leaves(self, v: int, out: list[int]):
        # DFS collecting suffix starts from leaves
        node = self.nodes[v]
        if len(node.children) == 0:
            out.append(node.suf)
            return
        for k in node.children:
            self._collect_leaves(node.children[k], out)

    def occurrences(self, pattern: list[int]) -> list[int]:
        # return all start positions of pattern in original string/array (excluding terminal-only suffix)
        v = self.follow(pattern)
        if v == -1:
            return []
        res = []
        self._collect_leaves(v, res)

        # filter out occurrences that start at the terminal position (n-1)
        # and also exclude those that would run past the original (n-1 is terminal)
        orig_n = self.n - 1
        pat_len = len(pattern)
        ans = []
        for p in res:
            if p < orig_n and p + pat_len <= orig_n:
                ans.append(p)
        return ans


S = input()
ls = [ord(s) for s in S]
cst = CompressedSuffixTree(ls)
nodes = cst.nodes
N = len(nodes)
ln = [node.end - node.start for node in nodes]
dp = [0] * N
checked = [False] * N
checked[0] = True
# print([n.children for n in nodes])


def dfs(v):
    win = False
    for nv in nodes[v].children.values():
        if dfs(nv): win = True; break
    return win

res = dfs(cst.root)
print(res)