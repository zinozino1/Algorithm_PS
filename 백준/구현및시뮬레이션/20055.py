# 실버1-컨베이어벨트

import copy
from collections import deque
import itertools as it

# 14:16-14:59


def sol():

    # 내구도가 0인 칸의 개수가 k개 이상이라면 종료
    n, k = map(int, input().split())
    belt = list(map(int, input().split()))
    robot = [0]*n
    top = 0
    bot = n-1
    cnt = 0
    while True:

        # 종료조건
        if belt.count(0) > k-1:
            break

        # 벨트 회전
        curr = belt.pop()
        belt.insert(0, curr)

        # 로봇 회전
        rob = robot.pop()
        robot.insert(0, 0)

        # 로봇 이동
        for i in range(n-1, -1, -1):
            if robot[i] == 1:
                if i == n-1:
                    robot[i] = 0
                else:
                    # 내구도 0이상, 로봇이 앞에 없어야 함
                    if belt[i+1] > 0 and robot[i+1] == 0:
                        robot[i+1] = robot[i]
                        robot[i] = 0
                        belt[i+1] -= 1

        # 로봇 올리기
        if belt[top] > 0 and robot[top] == 0:
            belt[top] -= 1
            robot[top] = 1

        cnt += 1

    print(cnt)


sol()
