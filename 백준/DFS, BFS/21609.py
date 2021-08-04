# 골드2 - 상어중학교
# bfs 구현 시뮬레이션

# 삼전 기출
# drop과 find가 중요했음 모두 bfs로 처리

from collections import deque


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
res = 0


def remove(x, y):
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    q = deque()
    q.append((x, y))
    init = grid[x][y]
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            grid[qx][qy] = -2
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0 and (grid[nx][ny] == 0 or grid[nx][ny] == init):
                    q.append((nx, ny))
                    visited[nx][ny] = 1


def find(x, y):
    q = deque()
    q.append((x, y))
    normal_blocks = []
    rainbow_blocks = []
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            if grid[qx][qy] != 0:
                normal_blocks.append((qx, qy, grid[qx][qy]))
            rainbow_blocks.append((qx, qy, grid[qx][qy]))
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and (grid[nx][ny] == 0 or grid[nx][ny] == grid[x][y]):
                    q.append((nx, ny))
                    check[nx][ny] = 1

    normal_blocks.sort(key=lambda x: (x[0], x[1]))
    size = len(rainbow_blocks)
    rainbow_num = len([r for r in rainbow_blocks if r[2] == 0])
    axisx = normal_blocks[0][0]
    axisy = normal_blocks[0][1]

    return (size, rainbow_num, axisx, axisy)


def rotate():
    tmp = [layer[:] for layer in grid]

    for p in range(n):
        for q in range(n):
            grid[n-q-1][p] = tmp[p][q]


def drop():
    for p in range(n):
        candi = []
        for q in range(n):
            target = grid[q][p]
            if target != -1 and target != -2:
                candi.append((q, p))

        while candi:
            x, y = candi.pop()

            while True:
                if x == n-1:
                    break
                if grid[x+1][y] == -1:
                    break
                if grid[x+1][y] >= 0:
                    break
                grid[x+1][y], grid[x][y] = grid[x][y], grid[x+1][y]
                x += 1


while True:
    check = [[0]*n for _ in range(n)]
    group = []
    for i in range(n):
        for j in range(n):
            if check[i][j] == 0 and grid[i][j] != -1 and grid[i][j] != 0 and grid[i][j] != -2:
                check[i][j] = 1
                for k in range(n):
                    for l in range(n):
                        if grid[k][l] == 0:
                            check[k][l] = 0
                group.append(find(i, j))
    group.sort(key=lambda x: (-x[0], -x[1], -x[2], -x[3]))

    if all(g[0] < 2 for g in group):
        break

    # 가장 큰 블록 제거 + 점수
    remove(group[0][2], group[0][3])
    res += group[0][0] ** 2
    # 중력
    drop()
    # 90 회전 (반시계 )
    rotate()
    # 중력
    drop()

print(res)
