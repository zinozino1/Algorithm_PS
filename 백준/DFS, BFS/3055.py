# 골드5 - 탈출
# BFS

# 물의 좌표가 고슴도치 좌표에 영향을 주므로 물을 먼저 처리한다
# 물 좌표를 업데이트 할 때 큐에서 꺼낸 것을 업데이트 함
# 고슴도치 좌표 큐에서 꺼낸후 업뎃된 물 좌표 위에 있으면 continue

from collections import deque

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
init = []
b1, b2 = 0, 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == "*":
            init.append([i, j, 1])
        if grid[i][j] == "S":
            init.append([i, j, 0, 0])
        if grid[i][j] == "D":
            b1, b2 = i, j

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs():

    q = deque()
    for it in init:
        q.append(it)
    water_check = [[0]*m for _ in range(n)]
    niddle_check = [[0]*m for _ in range(n)]

    while q:
        # 물먼저 세팅하기위해 물 -> 고슴도치순으로 정렬
        q = deque(sorted(q, key=lambda x: (-x[2])))
        for _ in range(len(q)):
            curr = q.popleft()

            # 물
            if curr[2] == 1:
                grid[curr[0]][curr[1]] = "*"
                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and water_check[nx][ny] == 0 and grid[nx][ny] == ".":
                        q.append([nx, ny, 1])
                        water_check[nx][ny] = 1

            # 고슴도치
            elif curr[2] == 0:
                if (curr[0], curr[1]) == (b1, b2):
                    return curr[3]
                if grid[curr[0]][curr[1]] == "*":
                    continue
                for s in range(4):
                    nx = curr[0]+dx[s]
                    ny = curr[1]+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and grid[nx][ny] == "D":
                        return curr[3]+1
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and niddle_check[nx][ny] == 0 and grid[nx][ny] == ".":
                        q.append([nx, ny, 0, curr[3]+1])
                        niddle_check[nx][ny] = 1

    return "KAKTUS"


print(bfs())
