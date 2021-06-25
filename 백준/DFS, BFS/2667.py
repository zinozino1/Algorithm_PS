# 실버1-단지 번호 붙이기
# 매우 핵심적인 BFS문제(flood fill)
# 라벨링 기본이니 꼭 숙지

from collections import deque
n = int(input())

grid = [list(input().strip()) for _ in range(n)]
check = [[0]*n for _ in range(n)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    house_cnt = 1
    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            grid[curr[0]][curr[1]] = str(cnt)
            for s in range(4):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and grid[nx][ny] == '1':
                    check[nx][ny] = 1
                    q.append((nx, ny))
                    house_cnt += 1
    return house_cnt


cnt = 1
res = []
for i in range(n):
    for j in range(n):
        if check[i][j] == 0 and grid[i][j] == "1":
            check[i][j] = 1
            res.append(bfs(i, j, cnt))
            cnt += 1

res = sorted(res)
print(cnt-1)
for r in res:
    print(r)
