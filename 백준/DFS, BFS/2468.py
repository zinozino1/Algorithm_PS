# 실버1-안전영역
# BFS
# 풀이시간 : 17분

import sys
from collections import deque

n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_h = -sys.maxsize
min_h = sys.maxsize

res = sys.maxsize


def bfs(x, y):
    q = deque()
    q.append((x, y))
    check[x][y] = 1

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            copy_grid[curr[0]][curr[1]] = level
            for s in range(4):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and copy_grid[nx][ny] > h:
                    q.append((nx, ny))
                    check[nx][ny] = 1


for i in range(n):
    for j in range(n):
        if grid[i][j] > max_h:
            max_h = grid[i][j]
        if grid[i][j] < min_h:
            min_h = grid[i][j]

for h in range(max_h+1):
    island_cnt = 0
    copy_grid = [layer[:] for layer in grid]
    check = [[0] * n for _ in range(n)]
    level = -1
    for i in range(n):
        for j in range(n):
            if copy_grid[i][j] > h and check[i][j] == 0:
                bfs(i, j)
                level -= 1

    for i in range(n):
        for j in range(n):
            if copy_grid[i][j] < res:
                res = copy_grid[i][j]


print(-res)
