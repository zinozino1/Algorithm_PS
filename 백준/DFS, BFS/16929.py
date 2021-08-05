# 골드4 - two dots
# dfs cycle


# 다시 풀기

n, m = map(int, input().split())
grid = [list((input().strip())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def dfs(L, x, y, px, py):  # 이전 좌표
    global flag
    for s in range(4):
        nx = x+dx[s]
        ny = y+dy[s]

        if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 1 and (px, py) != (nx, ny) and len(cycle) > 3:
            res.add(tuple(cycle))
            return

        if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == grid[i][j]:
            check[nx][ny] = 1
            visited[nx][ny] = 1
            cycle.append((nx, ny))
            dfs(L+1, nx, ny, x, y)
            check[nx][ny] = 0
            cycle.pop()


visited = [[0]*m for _ in range(n)]  # 방문 여부 확인용
final = False
for i in range(n):
    for j in range(m):
        if visited[i][j] == 0:  # 모든 좌표를 돌리는 것이 아니라 알파벳 하나당 하나만 돌릴거므로
            visited[i][j] = 1
            check = [[0]*m for _ in range(n)]  # 백트래킹용
            res = set()  # 만약 사이클의 갯수를 센다면 유용할것
            check[i][j] = 1
            cycle = [(i, j)]
            flag = False
            dfs(0, i, j, -1, -1)
            if res:
                final = True
                break
    if final:
        break

if final:
    print("Yes")
else:
    print("No")
