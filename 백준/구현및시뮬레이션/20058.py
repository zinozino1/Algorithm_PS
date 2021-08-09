# 골드4 - 마법사 상어와 파이어스톰
# 시뮬레이션 + dfs

# 배열 회전이 관건

import sys
sys.setrecursionlimit(10 ** 5)

n, q = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(2**n)]
level = list(map(int, input().split()))

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(x, y):
    global cnt
    for d in range(4):
        nx = x+dx[d]
        ny = y+dy[d]

        if 0 <= nx <= 2**n-1 and 0 <= ny <= 2**n-1 and check[nx][ny] == 0 and grid[nx][ny] > 0:
            check[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)


for l in level:
    cnt = 0
    candi = []
    for i in range(0, 2**n, 2**l):
        if cnt % 2 == 0:
            for j in range(0, 2**n, 2**(l+1)):
                tmp = []
                for k in range(i, i+2**l):
                    tmp.append(grid[k][j:j+2**l])

                for k in range(2**l):
                    for s in range(2**l):
                        grid[k+i][s+j] = tmp[2**l-1-s][k]
        else:
            for j in range(2**l, 2**n, 2**(l+1)):
                tmp = []
                for k in range(i, i + 2 ** l):
                    tmp.append(grid[k][j:j + 2 ** l])

                for k in range(2**l):
                    for s in range(2**l):
                        grid[k+i][s+j] = tmp[2**l-1-s][k]
        cnt += 1

    ice_cnt = [[0]*2**n for _ in range(2**n)]
    for i in range(2**n):
        for j in range(2**n):
            for d in range(4):
                ni = i+dx[d]
                nj = j+dy[d]
                if 0 <= ni <= 2**n-1 and 0 <= nj <= 2**n-1 and grid[ni][nj] > 0:
                    ice_cnt[i][j] += 1

    for i in range(2 ** n):
        for j in range(2 ** n):
            if ice_cnt[i][j] < 3 and grid[i][j] > 0:
                grid[i][j] -= 1


# 다 끝나고 얼음 개수 세기 & 덩어리 갯수 세기

for g in grid:
    print(g)
res1 = 0
for i in range(2**n):
    for j in range(2**n):
        res1 += grid[i][j]

res2 = -1e9
check = [[0]*2**n for _ in range(2**n)]
for i in range(2**n):
    for j in range(2**n):
        if check[i][j] == 0 and grid[i][j] > 0:
            cnt = 1
            check[i][j] = 1
            dfs(i, j)
            res2 = max(res2, cnt)

print(res1)
print(res2)
