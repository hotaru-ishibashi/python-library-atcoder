from atcoder.string import suffix_array
from bisect import bisect_left, bisect_right

def search(S, T):
    suffixes = suffix_array(S)
    tl = len(T)
    l = bisect_left(suffixes, T, key=lambda x: S[x:x+tl])
    r = bisect_right(suffixes, T, key=lambda x: S[x:x+tl])

    return suffixes[l:r]
