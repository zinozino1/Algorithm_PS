# 기본 bfs

from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def bfs(n, m, grid):
    check = [[0]*m for _ in range(n)]
    check[0][0] = 1
    q = deque()
    q.append((0, 0))
    cnt = 0

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            if (curr[0], curr[1]) == (n-1, m-1):
                return cnt+1
            for s in range(4):
                nx = curr[0]+dx[s]
                ny = curr[1]+dy[s]
                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0 and grid[nx][ny] == 1:
                    q.append((nx, ny))
                    check[nx][ny] = 1
        cnt += 1
    return -1


def solution(maps):

    return bfs(len(maps), len(maps[0]), maps)
