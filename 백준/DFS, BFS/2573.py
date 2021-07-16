# 골드4-빙산
# BFS
# python제출 시간초과 나길래 뭐지 싶었는데 pypy통과네 에라ㅏ이 ㅆㅂ 1시간 날림
# copy가 중요

from collections import deque

n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


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
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and copy_grid[nx][ny] != 0:
                    q.append((nx, ny))
                    check[nx][ny] = 1


time = 0
while True:
    copy_grid = [layer[:] for layer in grid]

    # 섬 나누기
    check = [[0]*m for _ in range(n)]
    level = 0
    for i in range(n):
        for j in range(m):
            if copy_grid[i][j] != 0 and check[i][j] == 0:
                bfs(i, j)
                level += 1

    if level > 1:
        print(time)
        break

    # 모두 0 이면 break

    zero_cnt = 0
    for g in grid:
        zero_cnt += g.count(0)
    if zero_cnt == n * m:
        print(0)
        break

    # 섬 주위 빙산 카운팅
    ice_cnt = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            tmp_cnt = 0
            if grid[i][j] != 0:
                for s in range(4):
                    ni = i+dx[s]
                    nj = j+dy[s]
                    if 0 <= ni <= n-1 and 0 <= nj <= m-1 and grid[ni][nj] == 0:
                        tmp_cnt += 1

            ice_cnt[i][j] = tmp_cnt

    # grid 업데이트
    for i in range(n):
        for j in range(m):
            if grid[i][j] - ice_cnt[i][j] < 0:
                grid[i][j] = 0
            else:
                grid[i][j] -= ice_cnt[i][j]

    time += 1
