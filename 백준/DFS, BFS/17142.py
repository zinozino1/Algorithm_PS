# 골드3-연구소3-DFS & BFS
# 비활성 바이러스와 빈칸을 채우는것이 다르다는 것을 나중에 알아서 에러 처리하기 빡셌음
# cnt는 그대로 BFS대로 가고 last는 '빈칸'이 채워졌을 때 +1 씩 해준다


import copy
import sys
from collections import deque
import itertools as it


def sol():
    global minN

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    def bfs(arr, copy):
        global minN
        q = deque()
        check = [[0] * n for _ in range(n)]
        for a in arr:
            q.append(a)
            check[a[0]][a[1]] = 1

        cnt = 0
        last = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if copy[curr[0]][curr[1]] != "*":
                    copy[curr[0]][curr[1]] = cnt

                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]

                    if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and (copy[nx][ny] == -1 or copy[nx][ny] == "*"):
                        if copy[nx][ny] == -1:
                            last = cnt + 1
                        check[nx][ny] = 1
                        q.append((nx, ny))

            cnt += 1

        flag = True
        for c in copy:
            if c.count(-1):
                flag = False
        if flag:
            if last < minN:
                minN = last

    n, m = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(n)]

    virus = []
    minN = 1e9

    for i in range(n):
        for j in range(n):
            if grid[i][j] == 2:
                virus.append((i, j))

    for tmp in it.combinations(virus, m):

        copy_grid = [g[:] for g in grid]

        for i in range(n):
            for j in range(n):
                if copy_grid[i][j] == 2 and (i, j) not in tmp:
                    copy_grid[i][j] = "*"
                if copy_grid[i][j] == 1:
                    copy_grid[i][j] = "-"
                if copy_grid[i][j] == 0:
                    copy_grid[i][j] = -1
        end_flag = True
        for x in copy_grid:
            if x.count(-1):
                end_flag = False
        if end_flag:
            minN = 0
            break
        bfs(tmp, copy_grid)

    if minN == 1e9:
        print(-1)
    else:
        print(minN)


sol()
