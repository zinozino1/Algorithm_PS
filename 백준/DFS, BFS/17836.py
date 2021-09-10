# 골드5 - 공주님을 구해라
# BFS

# 벽부수고 이동하기와 유사
# check를 3차원으로 구성해야 메모리초과 발생 x
# 그람을 획득한 경우는 그람을 획득하지 않은 경우와 별개의 경우라고 생각

# 이런식으로 구성
# [[1, 0], [1, 0], [1, 0], [1, 0], [1, 0]]
# [[0, 16], [0, 0], [0, 0], [0, 0], [1, 0]]
# [[0, 15], [1, 16], [1, 0], [1, 0], [1, 0]]
# [[0, 14], [0, 15], [1, 16], [0, 0], [0, 0]]
# [[1, 13], [1, 14], [1, 15], [0, 16], [0, 0]]
# [[0, 12], [0, 13], [1, 14], [0, 15], [0, 16]]

from collections import deque

n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y, 0))  # x,y,sword
    check = [[[0]*2 for _ in range(m)] for _ in range(n)]
    lv = 0
    while q:

        for _ in range(len(q)):
            qx, qy, sword = q.popleft()
            if qx == n-1 and qy == m-1:
                return lv
            if sword == 0:  # 그람 x
                for s in range(4):
                    nx = qx + dx[s]
                    ny = qy + dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny][1] == 0 and grid[nx][ny] == 2:
                        check[nx][ny][1] = lv
                        q.append((nx, ny, 1))
                    elif 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and check[nx][ny][0] == 0 and grid[nx][ny] == 0:
                        check[nx][ny][0] = 1
                        q.append((nx, ny, 0))
            else:  # 그람 o
                for s in range(4):
                    nx = qx+dx[s]
                    ny = qy+dy[s]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny][1] == 0:
                        check[nx][ny][1] = lv
                        q.append((nx, ny, 1))

        lv += 1

        if lv > t:
            return "Fail"
    return "Fail"


print(bfs(0, 0))
