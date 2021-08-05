# 골드5 - 마법사상어와 비바라기
# 구현 및 시뮬레이션

# 2차원 리스트 양옆, 대각선 연결 되어 있을 때 주의


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
orders = [tuple(map(int, input().split())) for _ in range(m)]
cloud = [[0] * n for _ in range(n)]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
dx2 = [-1, -1, 1, 1]
dy2 = [-1, 1, 1, -1]

init_cloud = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
for init in init_cloud:
    x, y = init
    cloud[x][y] = 1


def move(dir, dis):
    tmp_cloud = []
    for p in range(n):
        for q in range(n):
            if cloud[p][q] == 1:
                tmp_cloud.append((p, q))
                cloud[p][q] = 0

    res_cloud = []

    for tmp in tmp_cloud:
        tx, ty = tmp
        ntx = (tx + dx[dir] * dis) % n
        nty = (ty + dy[dir] * dis) % n

        if 0 <= ntx <= n - 1 and 0 <= nty <= n - 1:
            res_cloud.append((ntx, nty))

    for res in res_cloud:
        ntx, nty = res
        cloud[ntx][nty] = 1


for order in orders:
    d, s = order

    # 모든 구름 이동
    move(d, s)

    # 비가내려 바구니 물 양 1 증가
    water_block = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                grid[i][j] += 1
                water_block.append((i, j))

    # 구름 사라짐, 구름이 사라진 칸 배열 필요
    remove_cloud = []
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                remove_cloud.append((i, j))
                cloud[i][j] = 0

    # 물복사 버그 , 물이 증가한 칸 배열 필요

    for water in water_block:
        x, y = water
        cnt = 0
        for s in range(4):
            nx = x + dx2[s]
            ny = y + dy2[s]
            if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and grid[nx][ny] > 0:
                cnt += 1
        grid[x][y] += cnt

    # 구름 생김
    for i in range(n):
        for j in range(n):
            if grid[i][j] >= 2 and (i, j) not in remove_cloud:
                grid[i][j] -= 2
                cloud[i][j] = 1

res = 0
for g in grid:
    res += sum(g)
print(res)
