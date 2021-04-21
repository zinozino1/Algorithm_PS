# 골드4-드래곤커브
# 재귀로 푸려고 했으나 단순 반복과 규칙을 찾으면 풀 수 있는 문제

import copy
from collections import deque
import itertools as it


def sol():

    # 동북서남
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    def paint(dirs):

        tmp_x = x
        tmp_y = y
        grid[tmp_y][tmp_x] = 1
        for dir in dirs:
            tmp_x += dy[dir]
            tmp_y += dx[dir]
            if 0 <= tmp_x <= 100 and 0 <= tmp_y <= 100:
                grid[tmp_y][tmp_x] = 1

    n = int(input())
    grid = [[0] * 101 for _ in range(101)]

    for _ in range(n):
        x, y, d, g = map(int, input().split())
        dirs = [d]

        if g == 0:
            grid[y][x] = 1
            x += dy[d]
            y += dx[d]
            if 0 <= x <= 100 and 0 <= y <= 100:
                grid[y][x] = 1
            continue

        if g == 1:
            dirs.append((d+1) % 4)
            next_x = x
            next_y = y
            grid[next_y][next_x] = 1
            for dir in dirs:
                next_x += dy[dir]
                next_y += dx[dir]
                if 0 <= next_x <= 100 and 0 <= next_y <= 100:
                    grid[next_y][next_x] = 1

        else:
            dirs.append((d+1) % 4)
            for i in range(g-1):
                pos = 0
                for j in range(2**i):
                    dirs.append((dirs[j]+2) % 4)
                    pos += 1
                for j in range(pos, 2**(i+1)):
                    dirs.append(dirs[j])

            paint(dirs)

    cnt = 0
    for i in range(100):
        for j in range(100):
            if grid[i][j+1] == 1 and grid[i+1][j] == 1 and grid[i+1][j+1] == 1 and grid[i][j] == 1:
                cnt += 1

    print(cnt)


sol()
