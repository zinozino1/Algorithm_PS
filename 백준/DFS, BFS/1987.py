# 골드4 - 알파벳
# DFS + 백트래킹 or BFS
# in 연산자는 내부적으로 루프를 돌기 때문에 연산속도가 느리다
# 따라서 o(1)방법으로 중복 체킹을 해야함

# DFS
from collections import deque
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


# BFS 코드
# 좌표가 중복되도 되기 때문에 좌표 중복 체크배열을 두지 않았다.
# 큐에 문자열 concat값을 넣어 중복체크와 길이 비교를 동시에 한다.
# 그렇기에 레벨을 검사하지 않아도 된다.


# DFS가 좀 더 문제에 어울리는듯

r, c = map(int, input().split())
grid = [list(input().strip()) for _ in range(r)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

max_n = -1e9
check2 = set()


def bfs(x, y):
    global max_n
    q = deque()
    q.append((x, y, grid[x][y]))
    while q:
        for _ in range(len(q)):  # level을 사용하지 않는다면 있어도 되고 없어도 된다.
            c1, c2, c3 = q.popleft()
            max_n = max(max_n, len(c3))
            for s in range(4):
                nx = c1+dx[s]
                ny = c2+dy[s]
                if 0 <= nx <= r-1 and 0 <= ny <= c-1 and grid[nx][ny] not in c3 and (nx, ny, c3+grid[nx][ny]) not in check2:
                    check2.add((nx, ny, c3+grid[nx][ny]))
                    q.append((nx, ny, c3+grid[nx][ny]))


bfs(0, 0)
print(max_n)
