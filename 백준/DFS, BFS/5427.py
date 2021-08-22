# 골드4 - 불
# BFS

# 두 개의 로직을 하나의 BFS 안에서 처리하는 것이 중요

from collections import deque

T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, fire):
    q = deque()
    q.append((x, y, 1))
    sang_check = [[0]*n for _ in range(m)]
    fire_check = [[0]*n for _ in range(m)]
    sang_check[x][y] = 1

    for f in fire:
        fx, fy = f
        q.append((fx, fy, 2))
        fire_check[fx][fy] = 1

    level = 1

    while q:
        for _ in range(len(q)):
            qx, qy, op = q.popleft()
            if op == 1 and sang_check[qx][qy] == 0:
                continue
            # 상근
            if op == 1:
                for s in range(4):
                    nx = qx+dx[s]
                    ny = qy+dy[s]
                    if not (0 <= nx <= m-1 and 0 <= ny <= n-1):
                        return level
                    if 0 <= nx <= m-1 and 0 <= ny <= n-1 and sang_check[nx][ny] == 0 and grid[nx][ny] == ".":
                        q.append((nx, ny, 1))
                        sang_check[nx][ny] = 1
            # 불
            else:
                for s in range(4):
                    nx = qx+dx[s]
                    ny = qy+dy[s]
                    if 0 <= nx <= m-1 and 0 <= ny <= n-1 and fire_check[nx][ny] == 0 and grid[nx][ny] == ".":
                        if sang_check[nx][ny] == 1:
                            sang_check[nx][ny] = 0
                        grid[nx][ny] = "*"
                        q.append((nx, ny, 2))
                        fire_check[nx][ny] = 1

        level += 1

    return "IMPOSSIBLE"


for _ in range(T):
    n, m = map(int, input().split())
    grid = [list(input()) for _ in range(m)]
    fires = []
    sangx, sangy = -1, -1
    for i in range(m):
        for j in range(n):
            if grid[i][j] == "@":
                sangx, sangy = i, j
            if grid[i][j] == "*":
                fires.append((i, j))

    print(bfs(sangx, sangy, fires))
