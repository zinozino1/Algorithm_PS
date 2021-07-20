# 골드4 - 두동전
# BFS

# 엣지케이스 다 막아쓴데 반례가 뭔지 모르겠다
# + 코드 너무 더러워서 다시 풀어야함
from collections import deque

n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

coins = []
min_n = 1e9
for i in range(n):
    for j in range(m):
        if grid[i][j] == "o":
            coins.append((i, j))

q = deque()
for coin in coins:
    q.append(coin)
check = set()
level = 0
check.add((coins[0], coins[1]))
success_flag = False

while q:
    inner_flag = False
    if level >= 9:
        break
    for i in range(0, len(q)-1, 2):
        if inner_flag:
            break
        cx1, cy1 = q[i][0], q[i][1]
        cx2, cy2 = q[i+1][0], q[i+1][1]

        for s in range(4):
            nx1, ny1 = cx1 + dx[s], cy1 + dy[s]
            nx2, ny2 = cx2 + dx[s], cy2 + dy[s]
            coin_cnt = 0
            if (nx1 < 0 or nx1 > n-1) or (ny1 < 0 or ny1 > m-1):
                coin_cnt += 1
            if (nx2 < 0 or nx2 > n-1) or (ny2 < 0 or ny2 > m-1):
                coin_cnt += 1

            if coin_cnt == 1:
                print(level+1)
                success_flag = True
                inner_flag = True
                break
            else:
                continue

    if success_flag:
        break

    x1, y1 = q.popleft()
    x2, y2 = q.popleft()

    for s in range(4):

        nx1, ny1 = x1+dx[s], y1+dy[s]
        nx2, ny2 = x2+dx[s], y2+dy[s]

        if 0 <= nx1 <= n-1 and 0 <= ny1 <= m-1 and 0 <= nx2 <= n-1 and 0 <= ny2 <= m-1:
            f1, f2 = False, False
            if grid[nx1][ny1] == "." or grid[nx1][ny1] == "o":
                f1 = True
            else:
                f1 = False
            if grid[nx2][ny2] == "." or grid[nx2][ny2] == "o":
                f2 = True
            else:
                f2 = False
            if grid[nx1][ny1] == "o" and grid[nx2][ny2] == "#":
                f1, f2 = False, False
            if grid[nx2][ny2] == "o" and grid[nx1][ny1] == "#":
                f1, f2 = False, False

            if f1 and f2 and ((nx1, ny1), (nx2, ny2)) not in check:
                check.add(((nx1, ny1), (nx2, ny2)))
                q.append((nx1, ny1))
                q.append((nx2, ny2))
            elif f1 and not f2 and ((nx1, ny1), (x2, y2)) not in check:
                check.add(((nx1, ny1), (x2, y2)))
                q.append((nx1, ny1))
                q.append((x2, y2))
            elif not f1 and f2 and ((x1, y1), (nx2, ny2)) not in check:
                check.add(((x1, y1), (nx2, ny2)))
                q.append((x1, y1))
                q.append((nx2, ny2))
            elif not f1 and not f2 and ((x1, y1), (x2, y2)) not in check:
                check.add(((x1, y1), (x2, y2)))
                q.append((x1, y1))
                q.append((x2, y2))

    level += 1

if not success_flag:
    print(-1)

# 다시 풀이

# bfs 내부에서 for _ in range(len(q)): 를 사용하지 않는다면
# level의 개념을 활용할 수 없게 된다. -> 하나하나의 popleft가 level이
# 되어버리기 때문에 depth를 이용할 수 없음 따라서 q의 원소 안에 cnt라는 명시적 레벨을 넣어줘야함
# flag를 통해 bfs를 끝내는 것 보다 함수를 선언하고 return을 활용하자


n, m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

coins = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == "o":
            coins.append((i, j))

check = set()
check.add((coins[0][0], coins[0][1], coins[1][0], coins[1][1]))
level = 0


def bfs():
    global level
    q = deque()
    q.append((coins[0][0], coins[0][1], coins[1][0], coins[1][1], 0))

    while q:

        x1, y1, x2, y2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for s in range(4):
            nx1 = x1+dx[s]
            ny1 = y1+dy[s]
            nx2 = x2+dx[s]
            ny2 = y2+dy[s]

            if 0 <= nx1 <= n-1 and 0 <= ny1 <= m-1 and 0 <= nx2 <= n-1 and 0 <= ny2 <= m-1:
                if grid[nx1][ny1] == "#":
                    nx1, ny1 = x1, y1
                if grid[nx2][ny2] == "#":
                    nx2, ny2 = x2, y2
                if (nx1, ny1, nx2, ny2) not in check:
                    check.add((nx1, ny1, nx2, ny2))
                    q.append((nx1, ny1, nx2, ny2, cnt+1))
            elif 0 <= nx1 <= n-1 and 0 <= ny1 <= m-1:
                return cnt+1
            elif 0 <= nx2 <= n-1 and 0 <= ny2 <= m-1:
                return cnt+1
            else:
                continue
    else:
        return -1


print(bfs())
