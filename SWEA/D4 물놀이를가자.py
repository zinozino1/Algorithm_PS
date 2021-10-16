from collections import deque

T = int(input())


def bfs(arr):

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    q = deque()
    visited = [[0]*m for _ in range(n)]
    for a in arr:
        x, y = a
        q.append((x, y))
        visited[x][y] = 1
    dis = 0
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            res[qx][qy] = dis
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]

                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and visited[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        dis += 1


for t in range(T):
    n, m = map(int, input().split())
    grid = [list(input().strip()) for _ in range(n)]
    res = [[0]*m for _ in range(n)]
    waters = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == "W":
                waters.append((i, j))
    bfs(waters)
    tot = 0
    for r in res:
        tot += sum(r)
    print("#{} {}".format(t+1, tot))
