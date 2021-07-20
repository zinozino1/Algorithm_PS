# 골드4 - 알파벳
# DFS + 백트래킹
# in 연산자는 내부적으로 루프를 돌기 때문에 연산속도가 느리다
# 따라서 o(1)방법으로 중복 체킹을 해야함


r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_n = -1e9

alpha = [0]*26
alpha[ord(grid[0][0])-65] = 1

check = [[0]*c for _ in range(r)]
check[0][0] = 1


def dfs(L, x, y):
    global max_n
    if L > max_n:
        max_n = L
    for s in range(4):
        nx = x+dx[s]
        ny = y+dy[s]

        if 0 <= nx <= r-1 and 0 <= ny <= c-1 and alpha[ord(grid[nx][ny])-65] == 0 and check[nx][ny] == 0:
            alpha[ord(grid[nx][ny])-65] = 1
            check[nx][ny] = 1
            dfs(L+1, nx, ny)
            alpha[ord(grid[nx][ny])-65] = 0
            check[nx][ny] = 0


dfs(0, 0, 0)
print(max_n+1)
