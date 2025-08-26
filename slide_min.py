from collections import deque

def slide_min(A, K):
    que = deque()
    res = []
    for i, a in enumerate(A):
        while len(que) and (que[-1][0] >= a):
            que.pop()

        que.append((a, i))
        res.append(que[0][0])

        if que[0][1] <= i-K+1:
            que.popleft()

    return res[K-1:]