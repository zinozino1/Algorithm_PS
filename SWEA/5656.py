# DFS/BFS 완전탐색
# 패배 -> 전역변수 다루기가 어려웠음

import copy
import sys
from collections import deque
limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline


def sol():
    global max_cnt

    # 구슬이 명중한 벽돌은 상하좌우로 벽돌에 적힌 숫자 - 1만큼 같이 제거
    dx = [0, 1, 0]
    dy = [1, 0, -1]

    def reset(tmp_board):
        for i in range(w):
            tmp = []
            for j in range(h):
                if tmp_board[j][i] != 0:
                    tmp.append(tmp_board[j][i])
            for j in range(h - 1, -1, -1):
                if tmp:
                    tmp_board[j][i] = tmp.pop()
                else:
                    tmp_board[j][i] = 0

    def dfs(L, tmp_board, check):
        global max_cnt
        if L == n:
            cnt = 0
            for s in range(h):
                for a in range(w):
                    if tmp_board[s][a] != 0:
                        cnt += 1
            if max_cnt < cnt:
                max_cnt = cnt
            return

        else:
            start_x = -1
            start_y = -1
            for p in range(w):
                for q in range(h):
                    if tmp_board[p][q] != 0:
                        start_x = p
                        start_y = q
                        break

                check[start_x][start_y] = 1
                boom(0, start_x, start_y, tmp_board, check)
                reset(tmp_board)
                dfs(L+1, tmp_board, check)

    def boom(L, x, y, tmp_board, check):
        if 0 <= x <= h-1 and 0 <= y <= w-1:
            for s in range(3):
                nx = x + dx[s]
                ny = y + dy[s]
                for l in range(tmp_board[x][y]-1):
                    if 0 <= nx <= h - 1 and 0 <= ny <= w - 1 and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        boom(L + 1, nx+dx[s]*l, ny+dy[s]*l, tmp_board, check)
                        check[nx][ny] = 0
            tmp_board[x][y] = 0

    t = int(input())
    for _ in range(t):
        n, w, h = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(h)]

        for k in range(n):
            max_cnt = -1e9
            tmp_board = copy.deepcopy(board)
            # print("before")
            # for x in board:
            #   print(x)
            # print()
            check = [[0] * w for _ in range(h)]
            dfs(0, tmp_board, check)

            # print("after")
            # for x in board:
            #   print(x)
            # print()

            print(max_cnt)


sol()
