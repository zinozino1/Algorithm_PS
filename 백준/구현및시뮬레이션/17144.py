# 골드4-미세먼지야안녕

import copy
from collections import deque
import itertools as it

# 15:36 - 17:10 아 왤케 오래걸리지


def sol():

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    r, c, t = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(r)]

    cleaner = []
    for i in range(r):
        for j in range(c):
            if grid[i][j] == -1:
                cleaner.append((i, j))

    cleaner_top = cleaner[0]
    cleaner_bot = cleaner[1]

    time = 0
    while time < t:

        # 미세먼지 확산
        dusts = []
        for i in range(r):
            for j in range(c):
                if grid[i][j] != -1 and grid[i][j] != 0:
                    dusts.append((i, j, grid[i][j]))
                    grid[i][j] = 0

        for d in dusts:
            cnt = 0
            # 미세먼지 퍼져나가는 방향 세기
            for s in range(4):
                nx = d[0]+dx[s]
                ny = d[1]+dy[s]
                if 0 <= nx <= r-1 and 0 <= ny <= c-1 and grid[nx][ny] != -1:
                    cnt += 1
            # 미세먼지 나눠주기
            for s in range(4):
                nx = d[0]+dx[s]
                ny = d[1]+dy[s]
                if 0 <= nx <= r-1 and 0 <= ny <= c-1 and grid[nx][ny] != -1:
                    grid[nx][ny] += d[2] // 5
            # 미세먼지 확산 후 자신 업데이트
            grid[d[0]][d[1]] += d[2] - (d[2] // 5) * cnt

        # 공기 청정기

        # 공기청정기 위쪽
        # 모서리 값들 저장
        right_bot = grid[cleaner_top[0]][c-1]
        right_top = grid[0][c-1]
        left_top = grid[0][0]

        for i in range(c-2, 0, -1):
            grid[cleaner_top[0]][i+1] = grid[cleaner_top[0]][i]
        for i in range(cleaner_top[0]-1):
            grid[i][c-1] = grid[i+1][c-1]
        for i in range(c-1):
            grid[0][i] = grid[0][i+1]
        for i in range(1, cleaner_top[0]-1):
            grid[cleaner_top[0]-i][0] = grid[cleaner_top[0]-i-1][0]

        # 모서리 붙이기
        grid[cleaner_top[0]][1] = 0
        grid[1][0] = left_top
        grid[cleaner_top[0]-1][c-1] = right_bot
        grid[0][c-2] = right_top

        # 공기청정기 아래쪽
        # 모서리 값들 저장
        right_top2 = grid[cleaner_bot[0]][c - 1]
        right_bot2 = grid[r-1][c - 1]
        left_bot2 = grid[r-1][0]

        for i in range(c-2, 0, -1):
            grid[cleaner_bot[0]][i+1] = grid[cleaner_bot[0]][i]
        for i in range((r-1)-cleaner_bot[0]-1):
            grid[r-1-i][c-1] = grid[r-1-i-1][c-1]
        for i in range(1, c-1):
            grid[r-1][i-1] = grid[r-1][i]
        for i in range(1, (r-1)-cleaner_bot[0]-1):

            grid[cleaner_bot[0]+i][0] = grid[cleaner_bot[0]+i+1][0]

        # 모서리 붙이기
        grid[cleaner_bot[0]][1] = 0
        grid[cleaner_bot[0]+1][c-1] = right_top2
        grid[r-1][c - 2] = right_bot2
        grid[r-2][0] = left_bot2

        time += 1
    score = 0
    for i in range(r):
        for j in range(c):
            if grid[i][j] != -1 and grid[i][j] != 0:
                score += grid[i][j]
    print(score)


sol()
