# 골드4-인구이동

import copy
from collections import deque
import itertools as it

# 20:23-21:20


def sol():

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    n, l, r = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    def bfs(x, y):

        q = deque()
        q.append((x, y))
        check[x][y] = 1

        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= n-1 and l <= abs(grid[curr[0]][curr[1]] - grid[nx][ny]) <= r and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        q.append((nx, ny))
                        union[nx][ny] = union_cnt

    move_cnt = 0
    while True:

        union_cnt = 1
        union = [[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                check = [[0]*n for _ in range(n)]
                if union[i][j] != 0:
                    continue

                union[i][j] = union_cnt
                bfs(i, j)
                union_cnt += 1

        if union_cnt == n*n+1:
            break

        for k in range(1, union_cnt+1):
            nation_cnt = 0
            nation_popular = 0
            for i in range(n):
                for j in range(n):
                    if union[i][j] == k:
                        nation_cnt += 1
                        nation_popular += grid[i][j]
            for i in range(n):
                for j in range(n):
                    if union[i][j] == k:
                        grid[i][j] = nation_popular // nation_cnt

        move_cnt += 1
    print(move_cnt)


sol()
