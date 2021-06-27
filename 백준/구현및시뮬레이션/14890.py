# 골드3-경사로
# 빡구현 문제 시간을 줄여보자..

import copy
n, l = map(int, input().split())

grid = [list([0, 0] for _ in range(n)) for _ in range(n)]
val_grid = [list(map(int, input().split())) for _ in range(n)]
reverse_grid = []

for i in range(n):
    for j in range(n):
        grid[i][j][0] = val_grid[i][j]

for i, tmp in enumerate(zip(*grid)):
    reverse_grid.append(copy.deepcopy(list(tmp)))


def is_possible(grid):
    possible_cnt = 0
    for i in range(n):
        ormak_flag, naerimak_flag = True, True
        for j in range(n - 1):
            # 오르막
            if grid[i][j + 1][0] - grid[i][j][0] == 1:

                step_cnt = 0
                for k in range(j, j - l, -1):
                    if 0 <= k <= n - 1:
                        if grid[i][k][0] == grid[i][j][0] and grid[i][k][1] == 0:
                            step_cnt += 1
                            grid[i][k][1] = 1
                        else:
                            break
                    else:
                        break

                if step_cnt == l and (grid[i][j][0]-grid[i][j - l][0] <= 1 or j - 1 <= 0):
                    pass
                else:
                    ormak_flag = False
                    break

            # 내리막
            elif grid[i][j][0] - grid[i][j + 1][0] == 1:

                step_cnt = 0
                for k in range(j + 1, j + l + 1):
                    if 0 <= k <= n - 1:
                        if grid[i][k][0] == grid[i][j+1][0] and grid[i][k][1] == 0:
                            step_cnt += 1
                            grid[i][k][1] = 1
                        else:
                            break
                    else:
                        break

                if step_cnt == l and (grid[i][j][0] - grid[i][j + l][0] <= 1 or j - 1 <= 0):
                    pass
                else:
                    naerimak_flag = False
                    break
            # 평지
            elif grid[i][j][0] - grid[i][j + 1][0] > 1:
                naerimak_flag = False
            elif grid[i][j + 1][0] - grid[i][j][0] > 1:
                ormak_flag = False
            else:
                pass
        if ormak_flag and naerimak_flag:
            possible_cnt += 1
    return possible_cnt


print(is_possible(grid) + is_possible(reverse_grid))
