# 골드5-로봇청소기
# 최단경로 > BFS
# 기존 문제와 다르게 네방향 무조건 모두 돌리는 것이 아님. 청소할 곳이 있으면 그 곳 체크하고
# 바로 break해야함 네방향 다 돌렸는데 청소할 곳이 없으면 1) 뒤가 벽인 경우 2) 뒤가 청소한 곳인 경우
# 벽인 경우는 끝냄, 청소한 곳이면 후진
# 방향 설정하는 것도 매우 빈출임 -> %를 활용한 방향설정 매우 중요

import sys
from collections import deque
input = sys.stdin.readline


def sol():
    # 북 동 남 서
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    area = [list(map(int, input().split())) for _ in range(n)]
    area[r][c] = -1
    done_flag = False
    q = deque()
    q.append((r, c))
    tot = 1
    cnt = 2
    while q:

        if done_flag:
            break

        for i in range(len(q)):
            curr_pos = q.popleft()

            for _ in range(4):
                nx = curr_pos[0] + dx[(d - 1) % 4]
                ny = curr_pos[1] + dy[(d - 1) % 4]
                d = (d - 1) % 4

                if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and area[nx][ny] == 0:
                    q.append((nx, ny))
                    area[nx][ny] = cnt
                    cnt += 1
                    tot += 1
                    break

            else:
                nx = curr_pos[0] + dx[(d - 2) % 4]
                ny = curr_pos[1] + dy[(d - 2) % 4]
                if area[nx][ny] == 1:
                    done_flag = True
                    break
                else:
                    q.append((nx, ny))

    print(tot)


sol()
