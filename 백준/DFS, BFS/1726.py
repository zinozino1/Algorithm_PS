# 골드4 - 로봇
# BFS

# 반례 보고 AC맞음
# 전처리 정답체크, 루프검사

from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
x1, y1, d1 = map(int, input().split())
x1 -= 1
y1 -= 1
d1 -= 1
x2, y2, d2 = map(int, input().split())
x2 -= 1
y2 -= 1
d2 -= 1

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, d):
    q = deque()
    q.append((x, y, d))
    check = set()
    check.add((x, y, d))
    level = 0
    while q:
        for _ in range(len(q)):
            qx, qy, qd = q.popleft()
            if qx == x2 and qy == y2 and qd == d2:
                return level
            go = []
            turn = []

            # 일단 5가지 종류의 좌표를 다 담는다
            for s in range(5):
                if s == 0:
                    go.append((qx+dx[qd], qy+dy[qd], qd))
                elif s == 1:
                    go.append((qx+dx[qd]*2, qy+dy[qd]*2, qd))
                elif s == 2:
                    go.append((qx+dx[qd]*3, qy+dy[qd]*3, qd))
                elif s == 3:  # 왼
                    nx, ny, nd = qx, qy, qd
                    if qd == 0:
                        nd = 3
                    elif qd == 1:
                        nd = 2
                    elif qd == 2:
                        nd = 0
                    elif qd == 3:
                        nd = 1
                    turn.append((nx, ny, nd))
                elif s == 4:  # 오
                    nx, ny, nd = qx, qy, qd
                    if qd == 0:
                        nd = 2
                    elif qd == 1:
                        nd = 3
                    elif qd == 2:
                        nd = 1
                    elif qd == 3:
                        nd = 0
                    turn.append((nx, ny, nd))

            # 5가지 중에서 가능한것만 큐에 넣기

            # 회전 했을 떄
            for ne in turn:
                nex, ney, ned = ne
                if (nex, ney, ned) not in check:
                    check.add((nex, ney, ned))
                    q.append((nex, ney, ned))

            # go 했을 때
            for i, ne in enumerate(go):
                nex, ney, ned = ne
                flag = True
                for j in range(1, i+1):
                    nnx = qx+dx[qd]*j
                    nny = qy+dy[qd]*j
                    if not (0 <= nnx <= n-1 and 0 <= nny <= m-1) or grid[nnx][nny] == 1:
                        flag = False
                        break
                if 0 <= nex <= n-1 and 0 <= ney <= m-1 and grid[nex][ney] == 0 and (nex, ney, ned) not in check and flag:
                    check.add((nex, ney, ned))
                    q.append((nex, ney, ned))
        level += 1


print(bfs(x1, y1, d1))
