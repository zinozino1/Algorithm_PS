# 골드4 - 치즈
# BFS

# bfs는 0,0 에서 한 번만 돌리면 된다..
# 즉 내부에서 밖으로 가는 것이 아니라 밖에서 내부로 갈 수 있는 지를 bfs를 통해 한 번에 판단할 수 있다.


from collections import deque
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
end_cnt = n*m


def bfs(x, y):
    q = deque()
    q.append((x, y))
    air[x][y] = 1
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            for l in range(4):
                nqx = qx+dx[l]
                nqy = qy+dy[l]
                if 0 <= nqx <= n-1 and 0 <= nqy <= m-1 and air[nqx][nqy] == 0 and grid[nqx][nqy] == 0:
                    air[nqx][nqy] = 1
                    q.append((nqx, nqy))


Time = 0
while True:
    tmp_cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0:
                tmp_cnt += 1
    if tmp_cnt == end_cnt:
        break

    air = [[0]*m for _ in range(n)]
    bfs(0, 0)

    delete_candi = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                adj_cnt = 0
                for s in range(4):
                    nx = i+dx[s]
                    ny = j+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and grid[nx][ny] == 0 and air[nx][ny] == 1:
                        adj_cnt += 1
                if adj_cnt >= 2:
                    delete_candi.append((i, j))

    for delete in delete_candi:
        x, y = delete
        grid[x][y] = 0

    Time += 1

print(Time)
