# 골드4-마법사상어와 토네이도

import copy
from collections import deque
import itertools as it


def sol():
    global res
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    sdx1 = [(0, -1), (1, 0), (0, 1), (-1, 0)]
    sdx2 = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
    sdx3 = [(0, -2), (2, 0), (0, 2), (-2, 0)]

    def calculate_sand(x, y, dir):
        global res

        score = 0

        tmp_dir1 = dir
        tmp_dir2 = dir
        tmp_dir3 = dir
        order = [["a"], [7], ["x"], [7], [10], [
            10], [1], [1], [5], [2], ["no"], [2]]
        for i in range(len(order)):
            if 0 <= i <= 3:
                order[i].append(sdx1[tmp_dir1])
                tmp_dir1 = (tmp_dir1 + 1) % 4
            elif 3 < i <= 7:
                order[i].append(sdx2[tmp_dir2])
                tmp_dir2 = (tmp_dir2 + 1) % 4
            else:
                order[i].append(sdx3[tmp_dir3])
                tmp_dir3 = (tmp_dir3 + 1) % 4

        a_pos = None
        inner_score = 0
        for o in order:
            percent = o[0]
            pos = o[1]

            if percent == "x" or percent == "no":
                continue
            elif percent == "a":
                a_pos = (x + pos[0], y + pos[1])

            else:
                # 안인 경우
                if 0 <= x + pos[0] <= n - 1 and 0 <= y + pos[1] <= n - 1:
                    grid[x + pos[0]][y + pos[1]
                                     ] += int(grid[x][y] * percent / 100)
                    inner_score += int(grid[x][y] * percent / 100)
                # 밖인 경우
                else:
                    score += int(grid[x][y] * percent / 100)
                    inner_score += int(grid[x][y] * percent / 100)
        if 0 <= a_pos[0] <= n - 1 and 0 <= a_pos[1] <= n - 1:
            grid[a_pos[0]][a_pos[1]] += grid[x][y] - inner_score
        else:
            score += grid[x][y] - inner_score
        grid[x][y] = 0

        return score
        # 밖으로 나간 모래 양 계산

    def bfs(x, y):
        global res
        dir = 0
        lv = 0
        iter_cnt = 1
        q = deque()
        q.append((x, y))
        check = [[0] * n for _ in range(n)]
        check[x][y] = 1
        while q:

            if lv % 2 == 0 and lv != 0:
                iter_cnt += 1
            for _ in range(len(q)):
                curr = q.popleft()
                tornado[curr[0]][curr[1]] = 1

                # 토네이도 쪽에 모래가 있다면
                if grid[curr[0]][curr[1]] != 0:
                    res += calculate_sand(curr[0], curr[1], dir - 1)

                # depth 지정
                for k in range(1, iter_cnt + 1):

                    nx = curr[0] + dx[dir] * k
                    ny = curr[1] + dy[dir] * k

                    if 0 <= nx <= n - 1 and 0 <= ny <= n - 1 and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        q.append((nx, ny))
                    else:
                        break

            lv += 1
            dir = (dir + 1) % 4

    n = int(input())
    grid = [list(map(int, input().split())) for _ in range(n)]
    tornado = [[0] * n for _ in range(n)]
    start_x, start_y = n // 2, n // 2
    res = 0
    bfs(start_x, start_y)
    print(res)


sol()
