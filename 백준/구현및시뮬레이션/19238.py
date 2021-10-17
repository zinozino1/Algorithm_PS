# 골드4 - 스타트 택시
# 시뮬레이션

from collections import deque

n, m, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())
tx -= 1
ty -= 1
people = []
for _ in range(m):
    tmp = list(map(int, input().split()))
    tmp = list(map(lambda x: x-1, tmp))
    grid[tmp[0]][tmp[1]] = 2
    people.append(tmp)

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(sx, sy, ex, ey, tx, ty):
    q = deque()
    q.append((sx, sy))
    visited = [[0] * n for _ in range(n)]
    visited[sx][sy] = 1
    dist = 0
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            if (qx, qy) == (ex, ey):
                return dist
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0 and (grid[nx][ny] == 2 or grid[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        dist += 1
    return -1  # 갈 수 없는 경우


def getcandi(x, y):
    q = deque()
    q.append((x, y))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    dist = 0
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            if grid[qx][qy] == 2:
                candi.append([qx, qy, dist])
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and visited[nx][ny] == 0 and (grid[nx][ny] == 2 or grid[nx][ny] == 0):
                    visited[nx][ny] = 1
                    q.append((nx, ny))
        dist += 1


res = 0
time = 0
while True:

    candi = []
    getcandi(tx, ty)

    if not candi:
        p_cnt = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 2:
                    p_cnt += 1
        if p_cnt > 0:  # 남은 승객은 있지만 태우지 못할 때
            res = -1
        break  # 태울 승객이 없을 때

    candi.sort(key=lambda x: (x[2], x[0], x[1]))
    target = candi[0][:]
    sx, sy = target[0], target[1]  # 택시 출발지
    ex, ey = -1, -1
    dist = target[2]  # 거리

    if fuel < dist:  # 승객 태울 위치까지 가는데 연료 부족한 경우
        res = -1
        break
    fuel -= dist  # 태우러 갈때 연료 감소

    for p in people:
        psx, psy, pex, pey = p  # 승객 출발지 ,도착지 정보
        if (psx, psy) == (sx, sy):
            ex, ey = pex, pey
            break

    dist = bfs(sx, sy, ex, ey, tx, ty)  # 승객 이동
    if dist == -1 or fuel < dist:
        res = -1
        break

    tx, ty = ex, ey
    fuel -= dist  # 승객 태우고 목적지 갈 때 연료 감소
    fuel += dist*2
    grid[sx][sy] = 0  # 승객 배달 완료
    time += 1


if res == -1:
    print(-1)
else:
    print(fuel)
