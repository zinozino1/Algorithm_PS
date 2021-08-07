# 골드2 - 빵집
# dfs + greedy

# 정답 코드 -> 백트래킹을 하지 않음 현재 경로가 아니라 다른 경로로 와도 똑같이 실패할 것이기 때문에
# 백트래킹하지 않고 막아놓는다.

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
dx = [-1, 0, 1]
dy = [1, 1, 1]
flag = False


def dfs(x, y):
    global res, flag
    if y == m-1:
        flag = True
        res += 1
        return
    else:
        for s in range(3):
            nx = x+dx[s]
            ny = y+dy[s]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == "." and not flag:
                check[nx][ny] = 1
                dfs(nx, ny)


res = 0
check = [[0]*m for _ in range(n)]
for i in range(n):
    check[i][0] = 1
    dfs(i, 0)
    flag = False
print(res)

# TLE 코드

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]
dx = [-1, 0, 1]
dy = [1, 1, 1]
flag = False


def dfs(x, y, tot):
    global minN, tmp
    if y == m-1:
        arr = []
        sum = 0

        for p in range(n):
            for q in range(m):
                if check[p][q] == 1:
                    arr.append((p, q))
                    sum += p+q
        if sum < minN:
            minN = sum
            tmp = arr[:]
        return
    else:
        for s in range(3):
            nx = x+dx[s]
            ny = y+dy[s]

            if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == "." and visited[nx][ny] == 0:
                check[nx][ny] = 1
                tot += nx+ny
                dfs(nx, ny, tot)
                check[nx][ny] = 0
                tot -= nx+ny


visited = [[0]*m for _ in range(n)]
res = 0
for i in range(n):
    check = [[0]*m for _ in range(n)]
    check[i][0] = 1
    tmp = []
    minN = 1e9
    dfs(i, 0, i)
    if tmp:
        res += 1
    for t in tmp:
        x, y = t
        visited[x][y] = 1

print(res)
