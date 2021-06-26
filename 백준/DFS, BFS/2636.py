# 골드5-치즈
# 치즈 엣지를 구하는 것이 관건 -> 엣지들은 BFS를 돌려서 격자 밖으로 나갈 수 있어야함

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def is_edge(x, y):
    q = deque()
    q.append((x, y))
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if curr[0] == 0 or curr[0] == n-1 or curr[1] == 0 or curr[1] == m-1:
                return True
            for s in range(4):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append((nx, ny))

    return False


cheese_arr = []
cnt = 0
while True:
    local_cheese_cnt = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                local_cheese_cnt += 1
    cheese_arr.append(local_cheese_cnt)
    if all(g.count(1) == 0 for g in grid):
        break
    check = [[0]*m for _ in range(n)]
    tmp_res = []
    for i in range(1, n-1):
        for j in range(1, m-1):
            if check[i][j] == 0 and grid[i][j] == 1:
                check[i][j] = 1
                if is_edge(i, j):
                    tmp_res.append((i, j))
                check = [[0] * m for _ in range(n)]

    for t in tmp_res:
        grid[t[0]][t[1]] = 0

    cnt += 1

print(cnt)
print(cheese_arr[len(cheese_arr)-2])
