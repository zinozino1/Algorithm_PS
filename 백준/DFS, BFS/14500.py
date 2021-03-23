# 14500-골드5-테트로미노
# 처음에 모든 경우를 다따져서 단순 이터레이션으로 푸려고 했으나 말도 안되는 짓이었음
# 알고보니 전형적인 flood fill 문제 -> DFS로 조짐
# 하지만 예외(DFS의 한계 - 절대 dfs로 예외처리 불가)가 있었고 그것은 단순 이터레이션으로 해결했음
# 참고로 python3로 하면 시간초과남 pypy로 해야함

import sys

input = sys.stdin.readline


def sol():
    global maxN
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]
    maxN = -1e9
    check = [[0]*m for _ in range(n)]

    def dfs(L, x, y, tot):
        global maxN

        if L == 3:
            if tot > maxN:
                maxN = tot
        else:
            for s in range(4):
                nx = x+dx[s]
                ny = y+dy[s]

                if 0 <= nx <= n-1 and 0 <= ny <= m-1 and check[nx][ny] == 0:
                    check[nx][ny] = 1
                    dfs(L+1, nx, ny, tot+board[nx][ny])
                    check[nx][ny] = 0

    for i in range(n):
        for j in range(m):
            check[i][j] = 1
            dfs(0, i, j, board[i][j])
            check[i][j] = 0

    for i in range(n):
        for j in range(m):
            dir = [[(0, -1), (0, 1), (-1, 0)],
                   [(0, 1), (-1, 0), (1, 0)],
                   [(0, 1), (0, -1), (1, 0)],
                   [(0, -1), (1, 0), (-1, 0)]]

            for k in range(4):
                tmp_sum = board[i][j]
                flag = False
                for s in range(3):
                    nx = i+dir[k][s][0]
                    ny = j+dir[k][s][1]
                    if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                        tmp_sum += board[nx][ny]
                    else:
                        flag = True

                if not flag:
                    if tmp_sum > maxN:
                        maxN = tmp_sum

    print(maxN)


sol()
