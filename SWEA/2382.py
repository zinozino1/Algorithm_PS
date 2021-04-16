# 시뮬레이션-미생물 격리
# DFS/BFS 완전탐색
# 드디어 풀었다

import copy
import sys
from collections import deque

limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline


def sol():
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    t = int(input())
    test_case = 1
    for _ in range(t):

        n, m, k = map(int, input().split())
        grid = [[0] * n for _ in range(n)]

        for i in range(k):
            x, y, num, dir = map(int, input().split())
            grid[x][y] = [x, y, num, dir]

        time = 0
        # 시간마다 돌아감
        while time < m:
            spores = []

            # 루프 한 번 돌때마다 grid 초기화
            for i in range(n):
                for j in range(n):
                    if grid[i][j] != 0:
                        spores.append(grid[i][j])
                        grid[i][j] = 0

            check = [[[0] for _ in range(n)] for _ in range(n)]

            for i in range(len(spores)):
                x = spores[i][0]
                y = spores[i][1]
                num = spores[i][2]
                dir = spores[i][3]

                nx = x + dx[dir - 1]
                ny = y + dy[dir - 1]

                # 이동하려는 곳에 군집이 있으면
                if grid[nx][ny] != 0:
                    grid[nx][ny][2] += spores[i][2]
                    if max(check[nx][ny]) < spores[i][2]:
                        grid[nx][ny][3] = spores[i][3]
                    check[nx][ny].append(spores[i][2])

                # 군집이 없음
                else:
                    # 군집체크
                    check[nx][ny].append(spores[i][2])
                    # 일단 옮기고
                    grid[nx][ny] = spores[i][::]
                    # 좌표 변경
                    grid[nx][ny][0] = nx
                    grid[nx][ny][1] = ny
                    # 벽이라면
                    if nx == 0 or nx == n - 1 or ny == 0 or ny == n - 1:
                        # 방향 반대로
                        if grid[nx][ny][3] == 1:
                            grid[nx][ny][3] = 2
                        elif grid[nx][ny][3] == 2:
                            grid[nx][ny][3] = 1
                        elif grid[nx][ny][3] == 3:
                            grid[nx][ny][3] = 4
                        elif grid[nx][ny][3] == 4:
                            grid[nx][ny][3] = 3
                        # 미생물 수 절반 감소
                        grid[nx][ny][2] //= 2
            time += 1

        res = 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] != 0:
                    res += grid[i][j][2]

        print("#%d %d" % (test_case, res))
        test_case += 1


sol()
