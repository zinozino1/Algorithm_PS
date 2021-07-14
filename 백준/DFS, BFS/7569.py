# 실버1-토마토
# BFS 활용 -> 3차원적으로 생각해야해서 삽질 많이 함
# 한 층 외곽의 토마토들은 밑 층이 아닌 외곽을 건들면 안된다.

from collections import deque

n, m, h = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m*h)]

visited = [[0]*n for _ in range(m*h)]

dx = [0, 1, 0, -1, m, -m]
dy = [1, 0, -1, 0, 0, 0]
ready_tomatos = []

for i in range(m*h):
    for j in range(n):
        if grid[i][j] == 1:
            ready_tomatos.append((i, j))


def bfs(tomatos):
    q = deque()
    for tomato in tomatos:
        q.append(tomato)
        visited[tomato[0]][tomato[1]] = 1

    level = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            grid[curr[0]][curr[1]] = level
            for s in range(6):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= m*h-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0 and grid[nx][ny] == 0:
                    if curr[0] % m == 0 and s == 3:
                        continue
                    if (curr[0]+1) % m == 0 and s == 1:
                        continue
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        level += 1
    return level-2


res = bfs(ready_tomatos)
fail_flag = False
for i in range(m*h):
    for j in range(n):
        if grid[i][j] == 0:
            fail_flag = True
            break

# for g in grid:
#   print(g)
if fail_flag:
    print(-1)
else:
    print(res)
