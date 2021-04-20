# 골드5-주사위
import copy
from collections import deque
import itertools as it

# 21:00-22:01


def sol():
    # 동서북남
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    n, m, x, y, k = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    orders = list(map(int, input().split()))

    cube_row = [0, 0, 0, 0]
    cube_col = [0, 0, 0, 0]

    top = 0
    bot = 2

    cube_pos_x = x
    cube_pos_y = y

    for order in orders:
        # grid 벗어나면 제외
        if cube_pos_x + dx[order - 1] < 0 or cube_pos_x + dx[order - 1] > n - 1 or cube_pos_y + dy[
                order - 1] < 0 or cube_pos_y + dy[order - 1] > m - 1:
            continue

        # 주사위 전개도 재배치

        # 가로 방향 움직임
        if order == 1:  # east
            curr = cube_row.pop(0)
            cube_row.append(curr)
            cube_col[top] = cube_row[top]
            cube_col[bot] = cube_row[bot]
        elif order == 2:  # west
            curr = cube_row.pop()
            cube_row.insert(0, curr)
            cube_col[top] = cube_row[top]
            cube_col[bot] = cube_row[bot]

        # 세로 방향 움직임
        elif order == 3:  # north
            curr = cube_col.pop(0)
            cube_col.append(curr)
            cube_row[top] = cube_col[top]
            cube_row[bot] = cube_col[bot]
        elif order == 4:  # south
            curr = cube_col.pop()
            cube_col.insert(0, curr)
            cube_row[top] = cube_col[top]
            cube_row[bot] = cube_col[bot]

        # 주사위 위치 변경
        cube_pos_x += dx[order - 1]
        cube_pos_y += dy[order - 1]

        # 지도 바닥이 0이라면
        if grid[cube_pos_x][cube_pos_y] == 0:
            grid[cube_pos_x][cube_pos_y] = cube_row[bot]
        # 아니라면
        else:
            cube_row[bot] = grid[cube_pos_x][cube_pos_y]
            cube_col[bot] = grid[cube_pos_x][cube_pos_y]
            grid[cube_pos_x][cube_pos_y] = 0

        print(cube_row[top])


sol()
