# 웜홀 조건 때문에 패배

import copy
from collections import deque


def sol():

    # 동서남북
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 블럭 방향 정의
    # (x,y,dir)
    b_dir = [[(0, -1, 2), (0, 1, 0), (-1, 0, 3), (1, 0, 1)],  # 1
             [(0, -1, 2), (-1, 0, 3), (1, 0, 1), (0, 1, 0)],  # 2
             [(1, 0, 1), (-1, 0, 3), (0, 1, 0), (0, -1, 2)],  # 3
             [(-1, 0, 3), (0, -1, 2), (0, 1, 0), (1, 0, 1)],  # 4
             [(0, -1, 2), (-1, 0, 3), (0, 1, 0), (1, 0, 1)]]  # 5

    t = int(input())

    for test_case in range(1, t+1):

        n = int(input())
        grid = [list(map(int, input().split())) for _ in range(n)]

        max_score = -1e9
        for i in range(n):
            for j in range(n):
                # 초기 방향 4가지
                for d in range(4):
                    score = 0

                    if grid[i][j] == 0:
                        pos_x, pos_y = i, j
                        dir = d
                        time = 0
                        in_wormhole = False
                        check_wormhole = [[0]*n for _ in range(n)]
                        while True:
                            if pos_x < 0 or pos_x > n-1 or pos_y < 0 or pos_y > n-1:
                                break

                            # 시작 위치로 돌아오면  break
                            if time != 0 and pos_x == i and pos_y == j:
                                if pos_x + dx[dir] < 0 or pos_y + dy[dir] < 0:
                                    score -= 1
                                break

                            # 기본
                            if grid[pos_x][pos_y] == 0 and (pos_x != 0 and pos_x != n-1 and pos_y != 0 and pos_y != n-1):
                                pos_x += dx[dir]
                                pos_y += dy[dir]

                            # 벽이고 벽에 아무것도 없을 때
                            elif grid[pos_x][pos_y] == 0 and (pos_x == 0 or pos_x == n-1 or pos_y == 0 or pos_y == n-1):

                                # 꼬라박는 곳이 벽일 때
                                if pos_x+dx[dir] < 0 or pos_y+dy[dir] < 0:
                                    dir = (dir + 2) % 4
                                    pos_x += dx[dir]
                                    pos_y += dy[dir]
                                    score += 1

                                # 시작이 벽일 때
                                else:
                                    pos_x += dx[dir]
                                    pos_y += dy[dir]

                            # 웜홀
                            elif 6 <= grid[pos_x][pos_y] <= 10:

                                # 웜홀 드갔을 경우
                                print((pos_x, pos_y))
                                if not in_wormhole:
                                    check_wormhole[pos_x][pos_y] = 1
                                    # 동일한 번호를 가진 웜홀을 찾는다
                                    for p in range(n):
                                        find_flag = False
                                        for q in range(n):
                                            if p != pos_x and q != pos_y and grid[p][q] == grid[pos_x][pos_y] and check_wormhole[p][q] == 0:
                                                pos_x = p
                                                pos_y = q
                                                find_flag = True
                                                in_wormhole = True
                                                check_wormhole[p][q] = 1
                                                break
                                        if find_flag:
                                            break

                                # 웜홀 빠져나갔을 경우
                                else:
                                    in_wormhole = False
                                    pos_x += dx[dir]
                                    pos_y += dy[dir]

                            # 블랙홀
                            elif grid[pos_x][pos_y] == -1:

                                break

                            # 블럭
                            elif 1 <= grid[pos_x][pos_y] <= 5:
                                block_num = grid[pos_x][pos_y]
                                pos_x += b_dir[block_num - 1][dir][0]
                                pos_y += b_dir[block_num - 1][dir][1]
                                dir = b_dir[block_num - 1][dir][2]
                                score += 1

                            time += 1

                        if score > max_score:
                            max_score = score

        print("#%d %d" % (test_case, max_score))
        test_case += 1


sol()
