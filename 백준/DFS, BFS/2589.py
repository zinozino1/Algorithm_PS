# 골드5 보물섬
# 단순 BFS 활용

from collections import deque
import copy

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
tmp_grid = [layer[:] for layer in grid]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, label):
    q = deque()
    q.append((x, y))

    level = 0
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            grid[curr[0]][curr[1]] = str(level)
            for s in range(4):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == "L":
                    q.append((nx, ny))
                    check[nx][ny] = label
        level += 1


check = [[0]*m for _ in range(n)]
label = 1
global_max = -1e9
for i in range(n):
    for j in range(m):
        if check[i][j] == 0 and grid[i][j] == "L":
            check[i][j] = label
            bfs(i, j, label)
            label += 1
            max_num = -1e9
            for k in range(n):
                for l in range(m):

                    if not grid[k][l].isalpha():
                        if int(grid[k][l]) > max_num:
                            max_num = int(grid[k][l])
            if max_num > global_max:
                global_max = max_num

            grid = copy.deepcopy(tmp_grid)
            check = [[0] * m for _ in range(n)]

print(global_max)
