# 3190-골드5-구현
# 방향 경우의 수를 나머지 연산자로 구현한 것 중요
# 덱 사용
# 시작시간과 다음 행동의 시간차 유의

import sys
from collections import deque

input = sys.stdin.readline


def sol():

    n = int(input())
    apple_num = int(input())
    board = [[0]*n for _ in range(n)]

    for i in range(apple_num):
        x, y = map(int, input().split())
        board[x-1][y-1] = 1  # apple

    tot_time = 0

    dir_cnt = int(input())
    dir_info = [tuple(map(str, input().split())) for _ in range(dir_cnt)]
    snake = deque()
    snake.append((0, 0))

    # curr position
    curr_x = 0
    curr_y = 0

    # curr direction
    curr_dir = 0  # 0,1,2,3

    while True:
        if curr_dir == 0:  # east
            curr_y += 1
        elif curr_dir == 1:  # south
            curr_x += 1
        elif curr_dir == 2:  # west
            curr_y -= 1
        else:  # north
            curr_x -= 1

        if curr_x < 0 or curr_x > n-1 or curr_y < 0 or curr_y > n-1:
          # 벽에 부딪힌 경우
            print(tot_time+1)
            break

        if (curr_x, curr_y) in snake:
          # 몸통에 부딪힌 경우
            print(tot_time+1)
            break

        snake.append((curr_x, curr_y))
        if board[curr_x][curr_y] == 0:
            snake.popleft()
        else:
            board[curr_x][curr_y] = 0

        tot_time += 1

        for i in range(dir_cnt):
            if int(dir_info[i][0]) == tot_time:
                if dir_info[i][1] == "D":
                    curr_dir = (curr_dir + 1) % 4
                else:
                    curr_dir = (curr_dir - 1) % 4


sol()
