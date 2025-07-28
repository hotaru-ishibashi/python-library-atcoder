
class CompletelyBinaryTree:
    def __init__(self, N):
        self.n = N
        self.depth = N.bit_length()

    def nth_next_lr(self, x, n):
        if x.bit_length() + n > self.depth:
            raise ValueError("depth is out of range")
        bl = x * 1<<n
        br = (x+1) * 1<<n
        br = min(self.n+1, br)
        return bl, br
    

    def k_dist_count(self, x, k):
        if k == 0: return 1
        xdepth = x.bit_length()
        res = 0

        if xdepth + k <= self.depth:
            l, r = self.nth_next_lr(x, k)
            res += max(0, r - l)

        for back in range(1, min(xdepth, k+1)):
            proceed = k - back
            curdepth = xdepth - back

            if curdepth + proceed > self.depth:
                continue

            if proceed == 0:
                res += 1
            else:
                backed_1 = x
                for _ in range(back-1):
                    backed_1 //= 2
                l1, r1 = self.nth_next_lr(backed_1, proceed-1)
                backed = backed_1 // 2
                l, r = self.nth_next_lr(backed, proceed)
                blen = r-l
                if blen > 0:
                    intersect = min(r, r1) - max(l, l1)
                    if intersect > 0:
                        blen -= intersect
                    res += blen

        return res