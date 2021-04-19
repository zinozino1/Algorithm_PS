# 기본적인 BFS문제

import copy
from collections import deque


def sol():

    def bfs(x, y):
        time = 0
        cnt = 0
        q = deque()
        q.append((x, y))

        while q:
            if time == l:
                break
            for _ in range(len(q)):
                curr = q.popleft()
                cnt += 1
                val = ternal[curr[0]][curr[1]]-1
                for s in range(len(dir[val])):
                    nx = curr[0]+dir[val][s][0]
                    ny = curr[1]+dir[val][s][1]

                    if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                        if ternal[nx][ny] == 0:
                            continue
                        for p in dir[ternal[nx][ny]-1]:
                            if (nx+p[0], ny+p[1]) == (curr[0], curr[1]) and check[nx][ny] == 0:
                                check[nx][ny] = 1
                                q.append((nx, ny))
                                break

            time += 1

        print("#%d %d" % (test_case, cnt))

    # 터널 종류 1,2,3,4,5,6,7
    dir = [[(-1, 0), (1, 0), (0, 1), (0, -1)],
           [(1, 0), (-1, 0)],
           [(0, 1), (0, -1)],
           [(-1, 0), (0, 1)],
           [(0, 1), (1, 0)],
           [(0, -1), (1, 0)],
           [(0, -1), (-1, 0)]]

    t = int(input())

    for test_case in range(1, t+1):
        n, m, r, c, l = map(int, input().split())
        ternal = [list(map(int, input().split())) for _ in range(n)]
        check = [[0]*m for _ in range(n)]
        check[r][c] = 1
        bfs(r, c)


sol()
