# 골드4 - 스타트 택시
# 시뮬레이션

# 모든 손님에 대해 BFS돌리다 TLE났음
# 한번만 BFS돌려도 된다. 어차피 거리만 구하면 되어서
# 그 다음 heap 사용해서 좌표순으로 정렬해준다


from collections import deque
import heapq

n, m, fuel = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
tx, ty = map(int, input().split())
tx -= 1
ty -= 1
persons = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    for j in range(4):
        persons[i][j] -= 1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def move(x, y):
    q = deque()
    q.append((x, y))
    check = [[0]*n for _ in range(n)]
    check[x][y] = 1
    level = 0
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            if qx == ox and qy == oy:
                return level
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and grid[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append((nx, ny))
        level += 1


def get_dis():  # 손님x,손님y
    q = deque()
    q.append((tx, ty))
    check = [[0]*n for _ in range(n)]
    check[tx][ty] = 1
    level = 0
    while q:
        for _ in range(len(q)):
            qx, qy = q.popleft()
            table[qx][qy] = level
            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0 and grid[nx][ny] == 0:
                    check[nx][ny] = 1
                    q.append((nx, ny))
        level += 1


for l in range(m):  # 손님 수만큼 루프 돌리기

    # 각 손님과의 최단 거리계산
    dis = []
    table = [[-1]*n for _ in range(n)]
    get_dis()
    # for t in table:
    #   print(t)
    # print()

    minN = 1e9
    target = None
    heap = []
    for i in range(len(persons)):
        x1, y1, x2, y2 = persons[i]
        if table[x1][y1] < minN and table[x1][y1] != -1:
            minN = table[x1][y1]
            heapq.heappush(heap, [table[x1][y1], x1, y1, x2, y2, i])
    if heap:
        target = heapq.heappop(heap)

    if target is None or target[0] == -1:  # 도착지로 갈 수 없으면
        fuel = -1
        break

    # 손님 위치로 이동
    fuel -= target[0]
    if fuel < 0:  # 손님 위치로 이동하다 연료 바닥나면 브레이크
        break

    tx, ty = target[1], target[2]  # 택시좌표 업데이트
    ox, oy = target[3], target[4]  # 목적지 좌표

    # 목적지로 이동
    dis = move(tx, ty)
    if dis is None:  # 목적지로 갈 수 없는 경우
        fuel = -1
        break
    fuel -= dis  # 손님 싣고 이동

    if fuel < 0:  # 이동하다가 연료 바닥 나면 브레이크
        break
    fuel += dis * 2

    tx, ty = ox, oy

    # 손님 삭제
    del persons[target[5]]

if fuel < 0:
    print(-1)
else:
    print(fuel)
