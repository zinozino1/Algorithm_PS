# 실버2 - 배열 돌리기2
# 구현

n, m, r = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def lotate():
    tmp = [[0]*m for _ in range(n)]
    start_poses = []
    start_cnt = int(min(n, m)/2 + 0.5)

    for i in range(start_cnt):
        start_poses.append((i, i))

    check = [[0]*m for _ in range(n)]
    for start_pos in start_poses:
        x, y = start_pos
        cx, cy = x, y
        d = 0
        while True:
            nx = cx+dx[d]
            ny = cy+dy[d]

            if not (0 <= nx <= n-1 and 0 <= ny <= m-1) or check[nx][ny] == 1:
                d = (d + 1) % 4
                if d == 0:
                    break
                continue

            check[nx][ny] = 1
            tmp[nx][ny] = grid[cx][cy]
            cx, cy = nx, ny
    for i in range(n):
        for j in range(m):
            grid[i][j] = tmp[i][j]


for _ in range(r):
    lotate()

for g in grid:
    print(*g)
