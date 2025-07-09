from collections import deque

def grid_bfs(G, H, W, s):
    que = deque([s])
    dist = [[-1] * W for _ in range(H)]
    dist[s[0]][s[1]] = 0
    df = [[-1, 0], [0, -1], [1, 0], [0, 1]]

    while len(que):
        cx, cy = que.popleft()
        cd = dist[cx][cy]
        for dx, dy in df:
            nx, ny = cx+dx, cy+dy
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if G[nx][ny] =="#":
                continue
            if dist[nx][ny] != -1:
                continue
            dist[nx][ny] = cd + 1
            que.append([nx, ny])
    return dist