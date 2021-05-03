# 골드5-적록색약-BFS
# 매우쉬움

import itertools as it
from collections import deque


def sol():
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(x, y):
        q = deque()
        q.append((x, y))

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for s in range(4):
                    nx = curr[0] + dx[s]
                    ny = curr[1] + dy[s]
                    if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and check[nx][ny] == 0 and grid[nx][ny] == grid[x][y]:
                        check[nx][ny] = 1
                        q.append((nx, ny))

    n = int(input())
    grid = [list(input().strip()) for _ in range(n)]
    check = [[0] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                check[i][j] = 1
                cnt += 1
                bfs(i, j)

    for i in range(n):
        for j in range(n):
            if grid[i][j] == "R":
                grid[i][j] = "G"

    check = [[0] * n for _ in range(n)]
    disabled_cnt = 0
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0:
                check[i][j] = 1
                disabled_cnt += 1
                bfs(i, j)

    print(cnt, disabled_cnt)


sol()
