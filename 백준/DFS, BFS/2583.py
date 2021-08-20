# 실버1 - 영역 구하기
# BFS

# 최던거리가 아니라 갯수를 구하는거면 for s 루프 안에서 카운팅을 해줘야한다.

from collections import deque


n, m, k = map(int, input().split())
grid = [[0]*m for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for p in range(x1, x2):
        for q in range(y1, y2):
            grid[q][p] = 1


def bfs(x, y):
    q = deque()
    q.append((x, y))
    level = 1
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == 0:
                    q.append((nx, ny))
                    check[nx][ny] = 1
                    level += 1

    return level


check = [[0]*m for _ in range(n)]
cnt = 0
res = []
for i in range(n):
    for j in range(m):
        if check[i][j] == 0 and grid[i][j] == 0:
            cnt += 1
            check[i][j] = 1
            res.append(bfs(i, j))
print(cnt)
print(*sorted(res))
