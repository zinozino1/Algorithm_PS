# 실버1 - 데스나이트
# BFS

# 기본 BFS문제.

from collections import deque

n = int(input())
grid = [[0]*n for _ in range(n)]
r1, c1, r2, c2 = map(int, input().split())
grid[r1][c1], grid[r2][c2] = 1, 2

dir = [(-2, -1), (-2, 1), (0, -2), (0, 2), (2, -1), (2, 1)]
check = [[0]*n for _ in range(n)]


def bfs():
    q = deque()
    q.append((r1, c1))
    check[r1][c1] = 1
    level = 0
    while q:

        for _ in range(len(q)):
            x, y = q.popleft()

            for s in range(6):
                nx = x+dir[s][0]
                ny = y+dir[s][1]

                if 0 <= nx <= n-1 and 0 <= ny <= n-1 and check[nx][ny] == 0:
                    if nx == r2 and ny == c2:
                        return level+1
                    check[nx][ny] = 1
                    q.append((nx, ny))
        level += 1
    return -1


print(bfs())
