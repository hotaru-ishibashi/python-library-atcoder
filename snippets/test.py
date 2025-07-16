for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        u, v = query[1:]
    elif query[0] == 2:
        x = query[1:]
    # elif query[0] == 3: