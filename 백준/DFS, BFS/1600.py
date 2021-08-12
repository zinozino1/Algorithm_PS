# 골드4 - 말이 되고픈 원숭이
# BFS

# 트리 가지마다 k값을 다르게 판단해야하므로 큐에 kcnt를 넣어준다.

from collections import deque

k = int(input())
m, n = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
hdx = [-2, -1, 1, 2, 2, 1, -1, -2]
hdy = [1, 2, 2, 1, -1, -2, -2, -1]


def bfs(x, y, kcnt):
    q = deque()
    q.append((x, y, kcnt))
    check = set()
    check.add((x, y, kcnt))
    level = 0
    while q:
        for _ in range(len(q)):
            qx, qy, qcnt = q.popleft()
            if qx == n-1 and qy == m-1:
                return level

            if qcnt:  # 말처럼 이동할 수 있는 기회가 있음
                for h in range(8):
                    hqx = qx+hdx[h]
                    hqy = qy+hdy[h]
                    if 0 <= hqx <= n-1 and 0 <= hqy <= m-1 and (hqx, hqy, qcnt-1) not in check and grid[hqx][hqy] == 0:
                        q.append((hqx, hqy, qcnt-1))
                        check.add((hqx, hqy, qcnt-1))

            for s in range(4):
                nx = qx+dx[s]
                ny = qy+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and (nx, ny, qcnt) not in check and grid[nx][ny] == 0:
                    q.append((nx, ny, qcnt))
                    check.add((nx, ny, qcnt))

        level += 1
    return -1


print(bfs(0, 0, k))
