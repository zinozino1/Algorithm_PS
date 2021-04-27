# DFS/BFS 완전탐색
# 1) DFS로 벽돌이 떨어지는 모든 경우를 계산
# 2) DFS가지마다 tmp_board 복사해야함
# 3) 재귀 depth는 n만큼.

import copy
import sys
from collections import deque

limit_number = 15000
sys.setrecursionlimit(limit_number)
input = sys.stdin.readline


def sol():
    global min_cnt

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    # 벽돌 초기화
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

    # 모든 경우의 수
    def dfs(L, tmp_board):
        global min_cnt
        if L == n:
            cnt = 0
            for s in range(h):
                for a in range(w):
                    if tmp_board[s][a] != 0:
                        cnt += 1
            if min_cnt > cnt:
                min_cnt = cnt
            return

        else:
            start_x = -1
            start_y = -1
            for i in range(w):
                start_y = i
                for j in range(h):
                    if tmp_board[j][i] != 0:
                        start_x = j
                        break
                if start_x == -1:
                    continue
                # 가지마다 새로운 보드 복사
                tmp_board2 = copy.deepcopy(tmp_board)
                # 벽돌 파괴할 때 필요한 check 배열
                check = [[0] * w for _ in range(h)]
                check[start_x][start_y] = 1
                # 벽돌 파괴
                boom(0, start_x, start_y, tmp_board2, check)
                # 보드 리셋
                reset(tmp_board2)
                # 다음 가지 시작
                dfs(L+1, tmp_board2)

    # 벽돌 부수기
    def boom(L, x, y, tmp_board, check):
        if 0 <= x <= h - 1 and 0 <= y <= w - 1:
            # 4방향 모두 탐색
            for s in range(4):
                nx = x + dx[s]
                ny = y + dy[s]
                # 연쇄적 파괴(재귀) 벽돌에 있는 숫자만큼 재귀들어감
                # 모든 DFS 트리에서 tmp_board를 공유하므로 카피 안해도 된다.
                for l in range(tmp_board[x][y] - 1):
                    if 0 <= nx <= h - 1 and 0 <= ny <= w - 1 and check[nx][ny] == 0:
                        check[nx][ny] = 1
                        boom(L + 1, nx + dx[s] * l, ny +
                             dy[s] * l, tmp_board, check)
                        check[nx][ny] = 0
            # 파괴
            tmp_board[x][y] = 0

    test_case = 1
    t = int(input())
    for _ in range(t):
        n, w, h = map(int, input().split())
        board = [list(map(int, input().split())) for _ in range(h)]

        for k in range(n):
            min_cnt = 1e9
            tmp_board = copy.deepcopy(board)

            dfs(0, tmp_board)

        if min_cnt == 1e9:
            print("# %d %d" % (test_case, 0))
        else:
            print("# %d %d" % (test_case, min_cnt))
        test_case += 1


sol()
