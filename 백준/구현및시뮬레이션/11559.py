# 골드5 - puyopuyo
# 시뮬레이션 + BFS + DFS

# DFS에서 약간 헤맸다 다시 볼것..

from collections import deque

grid = [list(input().strip()) for _ in range(12)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def drop():
    for p in range(6):
        tmp = []
        for q in range(12):
            if grid[q][p] != ".":
                tmp.append(grid[q][p])
        for q in range(11, -1, -1):
            if tmp:
                grid[q][p] = tmp.pop()
            else:
                grid[q][p] = "."


def boom(L, k, l, init):
    grid[k][l] = "."
    for s in range(4):
        nx = k + dx[s]
        ny = l + dy[s]
        if 0 <= nx <= 11 and 0 <= ny <= 5 and check2[nx][ny] == 0 and grid[nx][ny] == init:
            check[nx][ny] = 1
            boom(L + 1, nx, ny, init)
            check[nx][ny] = 0


def bfs(x, y):
    q = deque()
    q.append((x, y))
    depth = 0
    while q:
        depth += len(q)
        for _ in range(len(q)):
            x1, y1 = q.popleft()
            for s in range(4):
                nx = x1 + dx[s]
                ny = y1 + dy[s]
                if 0 <= nx <= 11 and 0 <= ny <= 5 and check[nx][ny] == 0 and grid[nx][ny] == grid[x][y]:
                    q.append((nx, ny))
                    check[nx][ny] = 1
    return depth


res = 0
while True:
    avail = []
    check = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if grid[i][j] != "." and check[i][j] == 0:
                check[i][j] = 1
                curr = bfs(i, j)
                if curr >= 4:
                    avail.append((i, j))

    if not avail:
        break

    res += 1

    for ava in avail:
        x, y = ava
        check2 = [[0] * 6 for _ in range(12)]
        check2[x][y] = 1
        init = grid[x][y]
        boom(0, x, y, init)

    drop()

print(res)
