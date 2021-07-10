# 실버1-미로탐색
# 기본 BFS

from collections import deque
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
check = [[0]*m for _ in range(n)]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    level = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            grid[curr[0]][curr[1]] = level
            for s in range(4):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == "1":
                    check[nx][ny] = 1
                    q.append((nx, ny))
        level += 1


for i in range(n):
    for j in range(m):
        if grid[i][j] == "1":
            check[i][j] = 1
            bfs(i, j)

print(grid[n-1][m-1])

